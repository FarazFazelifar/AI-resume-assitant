class Prompts:
    PROFESSIONAL_SUMMARY = """
You are tasked with writing a professional summary for a resume using the information provided. Follow these steps:

1. Start with the individual's name (if available) and a concise sentence summarizing their professional identity, years of experience (derived from the experience section), and primary skills.
2. Highlight up to 3 key skills relevant to their career focus, based on the provided skills list.
3. Optionally include one measurable achievement or highlight from their experience, if provided.
4. End with a forward-looking statement reflecting their career aspirations.

### Formatting:
- Use markdown with the header `**Summary**:` followed by the summary.

### Rules:
- If any critical data (e.g., name or experience details) is missing, gracefully omit it.
- Ensure the summary is concise, professional, and tailored to the provided information.

#### Example Output:
**Summary**: [Name], an experienced software developer skilled in Python, Java, and cloud architecture. Proven success in enhancing system performance by 20% in previous roles. Seeking to leverage expertise in a dynamic technology environment.

"""



    WORK_EXPERIENCE = """
You are tasked with creating the work experience section for a resume. Follow these steps:

1. For each entry in the experience section, include:
   - The job title and company name in bold.
   - The employment dates in parentheses (if provided).
2. Use bullet points to summarize key responsibilities or achievements.

### Formatting:
- Use markdown for structure and clarity.

### Rules:
- Include only the information provided in the "experience" field.
- If specific data like dates or achievements is missing, omit gracefully.

#### Example Output:
**Software Engineer, TechCorp** (June 2018 - Present)  
- Designed and implemented scalable software solutions.  
- Reduced system latency by 15% through optimized algorithms.

"""


    SKILLS = """
You are tasked with writing the skills section for a resume. Use the following structure:

1. Organize skills into categories such as Technical Skills and Soft Skills.
2. List each skill as a bullet point without additional context.

### Formatting:
- Use markdown with section headers and bullet points for clarity.

### Rules:
- Include all skills provided; do not fabricate or expand beyond the given list.

#### Example Output:
**Skills**:
- **Technical Skills**:
  - Python
  - SQL
  - Data Analysis

- **Soft Skills**:
  - Team Leadership
  - Communication

"""

    EDUCATION = """
You are tasked with writing the education section for a resume. Use the following structure:

1. Include the degree and institution in bold.
2. Mention the graduation date in parentheses.
3. If additional details (e.g., coursework or honors) are provided, include up to two bullet points.

### Formatting:
- Use markdown to separate entries for clarity.

### Rules:
- Include only the information provided in the "education" field; omit unverifiable details.

#### Example Output:
**Bachelor of Science in Computer Science**  
**University of XYZ** (May 2020)  
- Relevant Coursework: Data Structures, Artificial Intelligence

"""

    CONTACT_INFO = """
You are tasked with formatting the contact information section of a resume. Use the following structure:

1. Include the individual's name at the top, bolded.
2. Below the name, list their email, phone number, and LinkedIn profile (if available), each on a new line.

### Formatting:
- Use plain text or markdown formatting for clarity.

### Rules:
- Include only the fields with available information; omit missing details.

#### Example Output:
**John Doe**  
johndoe@example.com  
(123) 456-7890  
[linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)

"""

class Skills:
   skills = ['Python', 'Machine Learning', 'Data Analysis', 'JavaScript', 'React', 
 'SQL', 'Cloud Computing', 'DevOps', 'Data Visualization', 'Artificial Intelligence', 
 'Deep Learning', 'Natural Language Processing', 'HTML', 'CSS', 'Node.js', 
 'Django', 'Flask', 'Git', 'GitHub', 'REST APIs', 'GraphQL', 'Agile Methodologies', 
 'Scrum', 'Kubernetes', 'Docker', 'AWS', 'Azure', 'Google Cloud', 'TensorFlow', 
 'PyTorch', 'Scikit-learn', 'Pandas', 'NumPy', 'Matplotlib', 'Tableau', 
 'Power BI', 'Big Data', 'Hadoop', 'Spark', 'Kafka', 'ETL Processes', 
 'Cybersecurity', 'Penetration Testing', 'Ethical Hacking', 'Information Security', 
 'Blockchain', 'Smart Contracts', 'Solidity', 'Cryptography', 'Java', 
 'C++', 'C#', 'PHP', 'Ruby on Rails', 'Swift', 'Objective-C', 'Kotlin', 
 'Android Development', 'iOS Development', 'UI/UX Design', 'Figma', 'Sketch', 
 'Adobe XD', 'Wireframing', 'Prototyping', 'SEO', 'SEM', 'Digital Marketing', 
 'Content Marketing', 'Copywriting', 'Salesforce', 'CRM Management', 'SAP', 
 'Oracle', 'Enterprise Architecture', 'Business Analysis', 'Project Management', 
 'JIRA', 'Trello', 'Asana', 'Leadership', 'Communication Skills', 'Teamwork', 
 'Problem Solving', 'Critical Thinking', 'Data Engineering', 'Database Management', 
 'NoSQL', 'MongoDB', 'Cassandra', 'Data Warehousing', 'Business Intelligence', 
 'R Programming', 'MATLAB', 'Statistical Analysis', 'Risk Management', 
 'Financial Modeling', 'Econometrics', 'Accounting', 'Microsoft Excel', 
 'VBA', 'Simulation', 'Robotics', 'Computer Vision', 'Embedded Systems', 
 'IoT Development', 'Autonomous Systems', 'Quantum Computing', 'Augmented Reality', 
 'Virtual Reality', 'Game Development', 'Unreal Engine', 'Unity', '3D Modeling', 
 'Blender', 'Maya', 'Animation', 'Video Editing', 'Final Cut Pro', 'Adobe Premiere Pro', 
 'Creative Writing', 'Technical Writing', 'Grant Writing', 'Public Speaking', 
 'Event Planning', 'Human Resources', 'Recruitment', 'Onboarding', 
 'Employee Training', 'Performance Management', 'Supply Chain Management', 
 'Logistics', 'Operations Research', 'Lean Manufacturing', 'Six Sigma', 
 'Quality Assurance', 'Regulatory Compliance', 'Healthcare IT', 
 'Medical Imaging', 'Bioinformatics', 'Clinical Research', 'Pharmacovigilance', 
 'Energy Systems', 'Renewable Energy', 'Mechanical Design', 'SolidWorks', 
 'AutoCAD', 'Civil Engineering', 'Structural Engineering', 'Geotechnical Engineering', 
 'Environmental Science', 'Urban Planning', 'GIS', 'ArcGIS', 'Remote Sensing', 
 'Customer Support', 'Technical Support', 'Help Desk', 'Troubleshooting', 
 'Product Management', 'Marketing Analytics', 'Behavioral Analysis', 
 'E-commerce', 'Dropshipping', 'Affiliate Marketing', 'Economics', 'Policy Analysis', 
 'Sociology Research', 'Educational Technology', 'Instructional Design', 
 'Curriculum Development', 'Teaching', 'Academic Writing', 'Research Methods', 
 'Linguistics', 'Translation', 'Interpreting', 'Foreign Language Proficiency', 
 'Music Theory', 'Composition', 'Sound Engineering', 'Audio Mixing', 
 'Performance Arts', 'Theater Production', 'Costume Design', 'Set Design', 
 'Photography', 'Photo Editing', 'Photoshop', 'Lightroom', 'Event Photography', 
 'Fashion Design', 'Pattern Making', 'Textile Design', 'Culinary Arts', 
 'Food Presentation', 'Menu Planning', 'Nutrition', 'Dietetics', 
 'Exercise Physiology', 'Personal Training', 'Sports Coaching', 
 'Kinesiology', 'First Aid', 'Emergency Response', 'Fire Safety', 
 'Social Media Management', 'Influencer Marketing', 'Podcasting', 
 'Video Production', 'Streaming', 'Community Management', 
 'Fundraising', 'Nonprofit Management', 'Volunteer Coordination', 
 'Legal Research', 'Contract Drafting', 'Litigation Support', 
 'Real Estate Management', 'Property Appraisal', 'Urban Economics', 
 'Public Administration', 'Policy Writing', 'Grant Administration', 
 'Library Science', 'Archival Management', 'Information Science', 
 'Data Curation', 'Digital Preservation', 'Astronomy', 'Astrophysics', 
 'Climate Science', 'Geology', 'Marine Biology', 'Zoology', 'Botany', 
 'Horticulture', 'Agricultural Science', 'Veterinary Medicine', 
 'Genetics', 'Molecular Biology', 'Biochemistry', 'Cell Biology', 
 'Microbiology', 'Immunology', 'Pharmaceutical Development', 
 'Chemical Engineering', 'Material Science', 'Nanotechnology', 
 'Thermodynamics', 'Fluid Mechanics', 'Aerodynamics', 
 'Aerospace Engineering', 'Control Systems', 'Signal Processing', 
 'Electronic Circuit Design', 'Power Electronics', 'Electric Vehicle Technology', 
 'Biomedical Engineering', 'Neuroscience', 'Cognitive Science', 
 'Psychology', 'Counseling', 'Social Work', 'Child Development', 
 'Educational Psychology', 'Cultural Anthropology', 'Archaeology', 
 'History Research', 'Art History', 'Museum Studies', 'Adaptability', 
 'Change Management', 'Client Relations', 'Collaboration', 'Creativity', 
 'Cross-functional Collaboration', 'Customer Service', 'Customer Success', 
 'Data Analytics', 'Diversity, Equity, and Inclusion (DEI)', 'Emotional Intelligence', 
 'Management', 'Marketing Strategy', 'Operations Management', 'Persuasion', 
 'Product Development', 'Relationship Building', 'Sales', 
 'Software Development Lifecycles (SDLC)', 'Stakeholder Management', 
 'Strategic Planning', 'Team Building', 'Team Management', 'UX Design', 
 'Video Production', 'Analytical Reasoning', 'Brainstorming', 'Data Mining', 
 'Diagnostics', 'Forecasting', 'Metric Interpretation', 'Organization', 
 'Reporting', 'Theorizing', 'Troubleshooting', 'CAD', 'Computer Design', 
 'Color Theory', 'Design-forward Thinking', 'Graphic Design', 'Interactive Design', 
 'Storytelling', 'Software Design', 'Typography', 'Visual Communication', 
 'Web Design', 'Open-mindedness', 'Flexibility', 'Stress Management', 
 'Proactive Learning', 'Curiosity', 'Innovation', 'Confidence', 
 'Product Knowledge', 'Enthusiasm', 'Tenacity', 'Negotiation', 
 'Networking', 'Active Listening', 'Nonverbal Communication', 
 'Presentation', 'Newsletters', 'Editing', 'Consulting', 'Delegating Tasks', 
 'Coaching', 'Relationship Management', 'Public Relations', 'Advertising', 
 'Market Research', 'Media Planning', 'Channel Marketing', 'Affiliate Marketing', 
 'Critical Thinking']
