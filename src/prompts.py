class Prompts:
    PROFESSIONAL_SUMMARY = """
You are tasked with generating a professional summary for an individual. Follow these steps carefully:

1. **Identify Key Strengths:** Consider the individual's skills, experiences, and accomplishments. Focus on core competencies such as leadership, technical expertise, problem-solving, communication skills, etc.

2. **Articulate Career Objectives:** Define clear and concise career goals, aligning them with the individual's strengths and aspirations. Be specific about industry or role preferences if mentioned.

3. **Tone and Structure:** Write in a formal and concise tone. Avoid generic phrases such as "Here is your generated answer." Instead, focus solely on presenting a professional summary that reflects the individual's unique strengths and career objectives.

4. **Clarity and Precision:** Ensure that the summary is direct and avoids any unnecessary elaboration. The summary should be easily digestible while maintaining a high level of professionalism and relevance to the targeted field.

- **Do not** include AI-generated phrases or fillers.
- **Do not** repeat key points; make sure the summary is compact yet comprehensive.

### Example Output Structure:
- **Key Strengths:** [List of key strengths, such as problem-solving, leadership, etc.]
- **Career Objectives:** [Concise statement of career goals, with industry or role focus if applicable.]

Do not include an introductory sentence like “Here is the summary…” or any disclaimers.

"""

    WORK_EXPERIENCE = """
You are tasked with generating detailed work experience entries for an individual. Follow these steps carefully:

1. **Focus on Achievements and Impact:** For each work experience, emphasize key achievements, measurable outcomes, and the specific impact the individual had in their role. Use data, metrics, and examples where applicable (e.g., “Increased sales by 20%” or “Led a team of 10 in a successful project completion”).

2. **Role and Responsibilities:** Clearly state the job title, the company name, and the time period of employment. Highlight the individual's main responsibilities, ensuring they align with the core duties of the role.

3. **Specific Contributions:** Detail the individual's contributions to the company or project. Be specific about what was achieved, how it was accomplished, and any recognition or awards received.

4. **Tone and Structure:** Write in a formal, professional tone. Avoid generic phrases such as “Here is your generated answer.” Focus on presenting factual, outcome-oriented entries. The entries should reflect both individual performance and overall impact on the organization.

5. **Clarity and Precision:** Ensure the entries are concise yet impactful, avoiding unnecessary elaboration. Each entry should demonstrate the individual's value in their role through specific accomplishments.

- **Do not** include AI-generated phrases or filler content.
- **Do not** over-generalize the impact; be precise and use quantifiable results where possible.

### Example Output Structure:
- **Job Title:** [e.g., Senior Software Engineer]
- **Company Name:** [e.g., XYZ Technologies]
- **Time Period:** [e.g., June 2019 - Present]
- **Key Responsibilities:** [List of responsibilities]
- **Achievements & Impact:** [Specific accomplishments with measurable results]

Ensure the content is written in a professional and concise manner, without unnecessary introduction or conclusion phrases.
"""

    SKILLS = """
You are tasked with listing and categorizing professional skills for an individual, providing relevant context for each. Follow these steps carefully:

1. **Identify Professional Skills:** Start by listing the key professional skills the individual possesses. These may include technical, soft, or transferable skills such as project management, programming languages, leadership, communication, etc.

2. **Categorize the Skills:** Group the skills into relevant categories. Common categories include:
   - **Technical Skills:** E.g., programming languages, software tools, data analysis
   - **Soft Skills:** E.g., leadership, communication, team collaboration
   - **Industry-Specific Skills:** E.g., financial modeling, research methodologies, healthcare regulations
   - **Transferable Skills:** E.g., problem-solving, time management, adaptability

3. **Provide Context:** For each skill, provide a brief explanation or example of how the individual has applied it in their career. If possible, mention the outcomes or impact of using these skills in specific roles or projects.

4. **Tone and Structure:** Write in a formal, professional tone. Avoid AI-generated phrases like “Here is your generated answer.” Present each skill in a clear and context-rich manner that highlights its relevance.

5. **Clarity and Precision:** The list should be concise yet comprehensive. Avoid excessive details, but ensure the context adds value to each skill, demonstrating its application.

- **Do not** include AI-generated filler content or introductory phrases.
- **Do not** generalize skills; provide context to show how each skill has been applied.

### Example Output Structure:
- **Category 1: Technical Skills**
  - **Skill:** [e.g., Python Programming]
    - **Context:** [Brief explanation of how it was applied in the individual's work, including measurable outcomes]
  
- **Category 2: Soft Skills**
  - **Skill:** [e.g., Leadership]
    - **Context:** [Example of leadership in a project, highlighting the impact]

Ensure the categorization is clear, with precise, context-driven explanations for each skill.
"""

    EDUCATION = """
You are tasked with listing and categorizing professional skills for an individual, providing relevant context for each. Follow these steps carefully:

1. **Identify Professional Skills:** Start by listing the key professional skills the individual possesses. These may include technical, soft, or transferable skills such as project management, programming languages, leadership, communication, etc.

2. **Categorize the Skills:** Group the skills into relevant categories. Common categories include:
   - **Technical Skills:** E.g., programming languages, software tools, data analysis
   - **Soft Skills:** E.g., leadership, communication, team collaboration
   - **Industry-Specific Skills:** E.g., financial modeling, research methodologies, healthcare regulations
   - **Transferable Skills:** E.g., problem-solving, time management, adaptability

3. **Provide Context:** For each skill, provide a brief explanation or example of how the individual has applied it in their career. If possible, mention the outcomes or impact of using these skills in specific roles or projects.

4. **Tone and Structure:** Write in a formal, professional tone. Avoid AI-generated phrases like “Here is your generated answer.” Present each skill in a clear and context-rich manner that highlights its relevance.

5. **Clarity and Precision:** The list should be concise yet comprehensive. Avoid excessive details, but ensure the context adds value to each skill, demonstrating its application.

- **Do not** include AI-generated filler content or introductory phrases.
- **Do not** generalize skills; provide context to show how each skill has been applied.

### Example Output Structure:
- **Category 1: Technical Skills**
  - **Skill:** [e.g., Python Programming]
    - **Context:** [Brief explanation of how it was applied in the individual's work, including measurable outcomes]
  
- **Category 2: Soft Skills**
  - **Skill:** [e.g., Leadership]
    - **Context:** [Example of leadership in a project, highlighting the impact]

Ensure the categorization is clear, with precise, context-driven explanations for each skill.
"""