import os
import logging
import yaml
import json
from typing import Dict, Any, List
from dataclasses import dataclass, field
from enum import Enum, auto
import ollama
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from utils import Prompts
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
import io
from html.parser import HTMLParser

MODEL_NAME = "llama3.2:3b-instruct-fp16"

class ResumeType(Enum):
    PROFESSIONAL = auto()
    ACADEMIC = auto()
    CREATIVE = auto()
    TECHNICAL = auto()

@dataclass
class UserProfile:
    name: str = ""
    email: str = ""
    phone: str = ""
    linkedin: str = ""
    resume_type: ResumeType = ResumeType.PROFESSIONAL
    skills: list[str] = field(default_factory=list)
    experience: list[Dict[str, Any]] = field(default_factory=list)
    education: list[Dict[str, Any]] = field(default_factory=list)

class ConfigManager:
    def __init__(self, config_path: str = 'config/config.yaml'):
        self.config_path = config_path
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('resume_ai.log'),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)

    def load_config(self) -> Dict[str, Any]:
        try:
            with open(self.config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            self.logger.warning(f"Config file not found.")
            return {}
        except Exception as e:
            self.logger.error(f"Error loading config: {e}")
            return {}

class ResumeGenerator:
    def __init__(self, user_profile: Dict[str, Any]):
        self.user_profile = user_profile
    
    def generate_resume_sections(self) -> Dict[str, Any]:
        try:
            professional_summary = ollama.chat(model=MODEL_NAME, messages=[
                {'role': 'system', 'content': Prompts.PROFESSIONAL_SUMMARY},
                {'role': 'user', 'content': f"Profile: {json.dumps(self.user_profile)}"}
            ])['message']['content']

            work_experience = ollama.chat(model=MODEL_NAME, messages=[
                {'role': 'system', 'content': Prompts.WORK_EXPERIENCE},
                {'role': 'user', 'content': f"Experience: {json.dumps(self.user_profile.get('experience', []))}"}
            ])['message']['content']

            skills = ollama.chat(model=MODEL_NAME, messages=[
                {'role': 'system', 'content': Prompts.SKILLS},
                {'role': 'user', 'content': f"Skills: {json.dumps(self.user_profile.get('skills', []))}"}
            ])['message']['content']

            education = ollama.chat(model=MODEL_NAME, messages=[
                {'role': 'system', 'content': Prompts.EDUCATION},
                {'role': 'user', 'content': f"Education: {json.dumps(self.user_profile.get('education', []))}"}
            ])['message']['content']

            contact_info = ollama.chat(model=MODEL_NAME, messages=[
                {'role': 'system', 'content': Prompts.CONTACT_INFO},
                {'role': 'user', 'content': f"""Profile: {json.dumps(self.user_profile.get("name", "")),
                                                        json.dumps(self.user_profile.get("email", "")),
                                                        json.dumps(self.user_profile.get("phone", "")),
                                                        json.dumps(self.user_profile.get("linkedin", "")),
                                                                   }"""}    
            ])['message']['content']

            return {
                'professional_summary': professional_summary,
                'work_experience': work_experience,
                'skills': skills,
                'education': education,
                'contact_info': contact_info
            }
        except Exception as e:
            logging.error(f"Resume generation error: {e}")
            return {}

class ResumePDFGenerator:
    @staticmethod
    def generate_pdf(resume_sections, output_filename='resume.pdf'):
        """
        Generate a PDF from markdown-formatted resume sections
        
        :param resume_sections: Dictionary of resume sections with markdown content
        :param output_filename: Path to save the output PDF
        """
        pdf_buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer, 
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
    
        story = []
        
        styles = getSampleStyleSheet()
        
        styles.add(ParagraphStyle(
            'ResumeHeader',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=12,
            textColor='navy',
            alignment=TA_LEFT
        ))
        
        styles.add(ParagraphStyle(
            'ResumeSectionHeader',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=10,
            textColor='darkblue',
            alignment=TA_LEFT
        ))
        
        styles.add(ParagraphStyle(
            'ResumeNormal',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            alignment=TA_LEFT
        ))
        
        class PDFHTMLParser(HTMLParser):
            def __init__(self, styles):
                super().__init__()
                self.story = []
                self.styles = styles
                self.current_style = styles['ResumeNormal']
                self.current_list = None
            
            def handle_starttag(self, tag, attrs):
                if tag == 'h1':
                    self.current_style = self.styles['ResumeHeader']
                elif tag == 'h2':
                    self.current_style = self.styles['ResumeSectionHeader']
                elif tag in ['p', 'div']:
                    self.current_style = self.styles['ResumeNormal']
                elif tag == 'strong':
                    self.current_style = ParagraphStyle(
                        'ResumeBold',
                        parent=self.styles['ResumeNormal'],
                        fontName='Helvetica-Bold'
                    )
                elif tag == 'em':
                    self.current_style = ParagraphStyle(
                        'ResumeItalic',
                        parent=self.styles['ResumeNormal'],
                        fontName='Helvetica-Oblique'
                    )
                elif tag in ['ul', 'ol']:
                    self.current_list = tag
            
            def handle_endtag(self, tag):
                if tag in ['h1', 'h2', 'p', 'div', 'strong', 'em']:
                    self.current_style = self.styles['ResumeNormal']
                if tag in ['ul', 'ol']:
                    self.current_list = None
            
            def handle_data(self, data):
                if data.strip():
                    if self.current_list == 'ul':
                        data = f'• {data}'
                    elif self.current_list == 'ol':
                        data = f'- {data}'
                    
                    self.story.append(Paragraph(data, self.current_style))
                    self.story.append(Spacer(1, 6))
        
        for section_name, section_content in resume_sections.items():
            html = markdown.markdown(section_content, extensions=['fenced_code', 'tables'])
            
            parser = PDFHTMLParser(styles)
            parser.feed(html)
            
            story.extend(parser.story)
            
            story.append(Spacer(1, 12))
        
        doc.build(story)
        
        with open(output_filename, 'wb') as f:
            f.write(pdf_buffer.getvalue())
        
        print(f"Resume PDF created successfully: {output_filename}")

def main():
    config_manager = ConfigManager()
    config = config_manager.load_config()

    user_profile = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "skills": ["Python", "Machine Learning", "Data Analysis"],
        "experience": [{
            "company": "TechCorp",
            "role": "Senior Developer",
            "duration": "2020-2023"
        }],
        "education": [{
            "institution": "Tech University",
            "degree": "Computer Science",
            "graduation_year": 2019
        }],
        "resume_type": "TECHNICAL"
    }

    resume_generator = ResumeGenerator(user_profile)
    resume_sections = resume_generator.generate_resume_sections()
    ResumePDFGenerator.generate_pdf(resume_sections)

if __name__ == "__main__":
    main()