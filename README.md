# ATS Resume Builder
![Screenshot 2025-03-26 151603](https://github.com/user-attachments/assets/76f187ce-3b1f-4a50-8091-277d4f9e8da3)


## Overview
The ATS Resume Builder is a web application designed to help users create optimized resumes that can pass through Applicant Tracking Systems (ATS). The application features an interactive front-end built with React, providing a seamless user experience for resume creation.

## Tech Stack
- **Frontend:**
  - React.js
  - Redux (for state management)
  - CSS3 / SCSS (for styling)
  - Axios (for API calls)

- **Backend:**
  - Django (Python)
  - Django REST Framework (for building APIs)
  - PostgreSQL (database)

- **Libraries:**
  - PDF Plumber (for extracting text from PDF resumes)
  - Spacy (for Natural Language Processing tasks)
  - Grok (for LLM integration)

- **Resume Creation:**
  - Interactive form to input personal details, education, experience, and skills.
  - Ability to upload existing resumes for analysis.

- **ATS Optimization:**
  - Analyzes resumes against job descriptions to provide feedback on ATS compatibility.
  - Scores resumes based on keyword matching and formatting.

- **Job Description Management:**
  - Create and manage job descriptions for comparison with resumes.

- **PDF Export:**
  - Download created resumes in PDF format.

- **Real-time Feedback:**
  - Instant scoring and suggestions for improving resume content.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ats-resume-builder.git
   cd ats-resume-builder

Install dependencies for the backend:
bash
cd backend
pip install -r requirements.txt

Set up the database:
Create a PostgreSQL database and update the database settings in settings.py.
Run migrations:
bash
python manage.py migrate

Start the backend server:
bash
python manage.py runserver

Install dependencies for the frontend:
bash
cd ../frontend
npm install

Start the frontend server:
bash
npm start

Usage
Open your browser and navigate to http://localhost:3000 to access the application.
Create an account or log in to start building your resume.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
Inspired by the need for effective resume building in the digital job market.
Thanks to the open-source community for the libraries and tools used in this project
