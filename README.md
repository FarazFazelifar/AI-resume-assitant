
# 🎯 AI Resume Generator

An intelligent, customizable resume generator built with **Streamlit**, **Python**, and integrated with advanced **AI models** to create professional, academic, technical, or creative resumes in PDF format. This project leverages **Llama 3.2** for generating resume content, and **ReportLab** for PDF creation, ensuring a seamless experience for users to craft personalized and high-quality resumes.

---

## 🛠️ Features

- **Dynamic Input Forms**:
  - Personal information (name, email, phone, LinkedIn).
  - Skills selection from a comprehensive list.
  - Customizable sections for work experience and education, allowing multiple entries.
  
- **AI-Powered Content Generation**:
  - Professional summaries, work experiences, skills categorization, and education descriptions tailored to user input.
  
- **PDF Resume Creation**:
  - Elegant formatting using **ReportLab**.
  - Markdown support for structured and clear layouts.
  
- **Interactive User Interface**:
  - Built using **Streamlit** for intuitive and user-friendly interactions.
  - Integrated animations for enhanced visual appeal via **streamlit-lottie**.

---

## 🔧 Technical Overview

### Architecture
1. **Frontend**:
   - Developed with **Streamlit** for form-based inputs and file handling.
   - Lottie animations for header and visual enhancements.

2. **Backend**:
   - **AI Model Integration**:
     - Utilizes **Llama 3.2:3b-instruct-fp16** for text generation.
     - APIs via **ollama** for querying the model.
   - **PDF Generation**:
     - Uses **ReportLab** to convert AI-generated markdown content into structured PDF resumes.
   - **Configuration Management**:
     - YAML-based configuration loader managed by `ConfigManager`.

3. **Utilities**:
   - Comprehensive skillsets and resume prompts encapsulated in utility files for modularity.

### Workflow
1. Users fill out personal, professional, and educational details in the Streamlit app.
2. Inputs are processed by the `ResumeGenerator` class:
   - Segregates data into sections (summary, work experience, education, skills).
   - Communicates with **Llama 3.2** to create tailored content.
3. The `ResumePDFGenerator` formats and compiles the content into a visually appealing PDF.
4. Users download the generated PDF directly from the web interface.

---

## 🚀 Installation

Follow these steps to set up and run the application locally:

### Prerequisites
- Python 3.8 or later
- A virtual environment manager (e.g., `venv` or `conda`)
- Streamlit installed
- **ollama** for AI integration
- Dependencies listed in `requirements.txt`

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/FarazFazelifar/AI-resume-assitant.git
   cd ai-resume-assistant
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scriptsctivate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run src/app.py
   ```

5. **Access the Application**:
   Open [http://localhost:8501](http://localhost:8501) (The page should open automatically. Also, it may use another port, you should check the bash output) in your browser to start using the AI Resume Generator.

---

## 🧩 Key Components

### 1. `app.py`
- Main entry point of the application.
- Handles the user interface using **Streamlit**.
- Provides dynamic forms for personal details, experience, and education sections.
- Connects with `ResumeGenerator` and `ResumePDFGenerator`.

### 2. `main.py`
- Core business logic for generating and formatting resume sections.
- Implements:
  - `ResumeGenerator`: Interacts with the AI model to generate content.
  - `ResumePDFGenerator`: Converts markdown content into formatted PDFs.
  - `ConfigManager`: Handles configuration settings via YAML files.

### 3. `utils.py`
- Contains:
  - `Prompts`: Predefined templates for AI-driven text generation.
  - `Skills`: A comprehensive list of skills categorized for easy selection.

---


## 📧 Contact

For queries, feedback, or suggestions, please reach out at [my LinkedIn page](https://www.linkedin.com/in/faraz-fazelifar/).

Enjoy creating professional resumes effortlessly with AI! 🚀
