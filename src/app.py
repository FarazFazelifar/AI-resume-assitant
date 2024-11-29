import streamlit as st
import json
from main import ResumeGenerator, ResumePDFGenerator
from streamlit_lottie import st_lottie

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def add_dynamic_fields(section, key_prefix):
    """Dynamically add input fields for experiences/education"""
    st.subheader(f"{section} Details")
    st.write(f"Enter information about your {section.lower()} below.")
    num_entries = st.number_input(
        f'Number of {section} entries',
        min_value=0, max_value=5, key=f'{key_prefix}_count'
    )
    entries = []
    
    for i in range(num_entries):
        with st.expander(f'{section} Entry {i + 1}'):
            entry = {}
            for field in ['company', 'role', 'duration'] if section == 'Experience' else ['institution', 'degree', 'graduation_year']:
                st.write(f"Enter the {field.replace('_', ' ')}.")
                entry[field] = st.text_input(field.replace('_', ' ').title(), key=f'{key_prefix}_{i}_{field}')
        entries.append(entry)
    
    return entries

def main():
    st.set_page_config(page_title="AI Resume Generator", layout="wide")
    
    # Lottie Animation for the header
    lottie_header = load_lottie_file("header.json")
    st_lottie(lottie_header, height=200, key="header")
    
    st.title('🎯 AI Resume Generator')
    st.write("Welcome to the AI Resume Generator! Fill out the fields below to create a professional resume tailored to your needs.")

    # Personal Information
    st.header("🔑 Personal Information")
    st.write("Provide your basic details to include in the resume.")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input('Full Name', placeholder="e.g., John Doe")
    with col2:
        email = st.text_input('Email', placeholder="e.g., john.doe@example.com")
    
    phone = st.text_input('Phone Number', placeholder="e.g., +1 234 567 890")
    linkedin = st.text_input('LinkedIn Profile (Username)', placeholder="e.g., john-doe")

    # Skills
    st.header("💼 Skills")
    st.write("Select your key skills to showcase in the resume.")
    skills = st.multiselect(
        'Select Skills', 
        ['Python', 'Machine Learning', 'Data Analysis', 'JavaScript', 'React', 
         'SQL', 'Cloud Computing', 'DevOps', 'Data Visualization']
    )
    
    # Dynamic Experience Entries
    experience = add_dynamic_fields('Experience', 'work')
    
    # Dynamic Education Entries
    education = add_dynamic_fields('Education', 'edu')
    
    # Resume Type Selection
    st.header("📄 Resume Preferences")
    st.write("Choose the type of resume you want to generate.")
    resume_type = st.selectbox(
        'Resume Type', 
        ['PROFESSIONAL', 'TECHNICAL', 'ACADEMIC', 'CREATIVE']
    )
    
    # Generate Resume Button
    if st.button('Generate Resume'):
        st.write("Processing your inputs to generate the resume...")
        user_profile = {
            "name": name,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "skills": skills,
            "experience": experience,
            "education": education,
            "resume_type": resume_type
        }
        
        with st.spinner("Generating Resume..."):
            # Generate Resume
            resume_generator = ResumeGenerator(user_profile)
            resume_sections = resume_generator.generate_resume_sections()
        
            # PDF Generation
            ResumePDFGenerator.generate_pdf(resume_sections)
        
        st.success('✅ Resume Generated Successfully!')
        with open('resume.pdf', 'rb') as pdf_file:
            st.download_button(
                label='📥 Download Resume',
                data=pdf_file.read(),
                file_name='resume.pdf',
                mime='application/pdf'
            )

if __name__ == "__main__":
    main()
