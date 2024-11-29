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
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from prompts import Prompts

MODEL_NAME = "llama3.1:8b-instruct-q8_0"

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

            return {
                'professional_summary': professional_summary,
                'work_experience': work_experience,
                'skills': skills,
                'education': education
            }
        except Exception as e:
            logging.error(f"Resume generation error: {e}")
            return {}

class ResumePDFGenerator:
    @staticmethod
    def generate_pdf(resume_data: Dict[str, Any], output_path: str = 'resume.pdf'):
        try:
            pdf = SimpleDocTemplate(output_path, pagesize=letter)
            styles = getSampleStyleSheet()
            content = []

            sections = [
                ('Professional Summary', resume_data.get('professional_summary', '')),
                ('Work Experience', resume_data.get('work_experience', '')),
                ('Skills', resume_data.get('skills', '')),
                ('Education', resume_data.get('education', ''))
            ]

            for title, text in sections:
                content.append(Paragraph(title, styles['Heading1']))
                content.append(Paragraph(text, styles['Normal']))
                content.append(Spacer(1, 12))

            pdf.build(content)
            logging.info(f"Resume PDF generated at {output_path}")
        except Exception as e:
            logging.error(f"PDF generation error: {e}")

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