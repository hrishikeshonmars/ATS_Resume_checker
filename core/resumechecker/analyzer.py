import pdfplumber
import json
import re
from groq import Groq  # ✅ Correct import for Groq API

API_KEY = "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"  # ✅ API key remains unchanged

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + '\n'
    return text.strip()

def analyze_resume_with_llm(resume_text: str, job_description: str) -> dict:
    prompt = f"""
I am an AI assistant analyzing resumes for software engineering applications.
Given a resume and a job description, extract the following details:

1. Identify all the skills mentioned in the resume.
2. Calculate the total years of experience.
3. Categorize the projects based on the domain (e.g., AI, web development, Cloud, etc.).
4. Rank the resume relevance based on the job description on a scale of 0 to 100.

Resume:
{resume_text}

Job Description:
{job_description}

Provide the output in valid JSON format with this structure:
{{
    "rank": "<percentage>",
    "skills": ["skill1", "skill2", "skill3"],
    "total_experience": "<number of years>",
    "project_category": ["category1", "category2", "category3"]
}}
"""

    try:
        client = Groq(api_key=API_KEY)  # ✅ Corrected Groq client initialization
        
        response = client.chat.completions.create(  # ✅ Fixed API method call
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        # ✅ Ensure response is valid
        if not response.choices or not response.choices[0].message.content:
            return {"status": False, "error": "Empty response from LLM"}

        result = response.choices[0].message.content.strip()

        # ✅ Debugging: Print raw response to check JSON format
        print("Raw LLM Response:", result)

        # ✅ Extract JSON content using regex
        match = re.search(r'\{.*\}', result, re.DOTALL)
        if match:
            json_text = match.group(0)  # Extract JSON part
            return json.loads(json_text)  # ✅ Convert JSON string to Python dictionary
        else:
            return {"status": False, "error": "No valid JSON found in response"}

    except Exception as e:
        print("Error:", str(e))
        return {"status": False, "error": str(e)}

def process_resume(pdf_path, job_description):
    try:
        resume_text = extract_text_from_pdf(pdf_path)
        data = analyze_resume_with_llm(resume_text, job_description)
        return data
    except Exception as e:
        print(e)
        return None
