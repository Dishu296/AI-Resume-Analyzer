# 🧠 AI Resume Analyzer

An AI-powered web application that analyzes resumes using **Natural Language Processing (NLP)** to evaluate skills, keywords, and job relevance.  
It calculates an **ATS (Applicant Tracking System) score**, identifies missing skills, and provides actionable suggestions to improve your resume — helping you get noticed by recruiters 🚀  

---

## 📸 Project Preview

| Upload Resume | Analysis Output |
|----------------|----------------|
| ![Interface](assets/interface.png) | ![Output](assets/sample_output.png) |

---

## 🎯 Features

✅ Extracts text from PDF and DOCX resumes  
✅ Matches keywords with a given job description  
✅ Generates ATS score (out of 100)  
✅ Displays matched keywords visually using WordCloud  
✅ Provides personalized improvement suggestions  
✅ Clean, user-friendly Streamlit interface  

---

## 🧠 Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| **Language** | Python |
| **Framework** | Streamlit |
| **NLP** | spaCy, NLTK |
| **Data Handling** | Pandas, Scikit-learn |
| **File Parsing** | PyPDF2, python-docx |
| **Visualization** | Matplotlib, WordCloud |
| **Deployment** | Streamlit Cloud / GitHub Pages |

---

## 📂 Folder Structure

 AI-Resume-Analyzer/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── .gitignore # Ignore files for GitHub
│
├── data/
│ ├── skills_list.csv # Dataset of common skills
│ └── sample_resume.pdf # Example resume
│
└── assets/
├── logo.png # Project/Company logo
├── interface.png # Screenshot of app UI


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
### 2️⃣ Install dependencies

pip install -r requirements.txt
    3️⃣ Download the spaCy model
python -m spacy download en_core_web_sm
    4️⃣ Run the Streamlit app
streamlit run app.py


Your app will open at 👉 http://localhost:8501/

💡 How It Works

Upload your resume (PDF or DOCX).

Paste a relevant job description.

The AI model extracts and compares key skills using spaCy NLP.

An ATS score (out of 100) is generated.

The app visualizes matched keywords with a WordCloud and provides tips for improvement.

🧾 Example Output

Resume Score: 82 / 100

Matched Keywords: Python, Machine Learning, Data Analysis, SQL

Suggestions:

Add keywords like “Power BI” and “Deep Learning”

Improve technical summary section

🌐 Deployment

You can deploy the project using Streamlit Cloud:

Go to https://share.streamlit.io

Connect your GitHub repository

Set the main file as app.py

Click Deploy

Example live link:

https://ai-resume-analyzer.streamlit.app

📚 Dataset Reference

The file data/skills_list.csv contains a collection of common technical and soft skills sourced from public job postings and open datasets.
You can modify or expand it to fit specific industries (e.g., Data Science, Web Dev, AI/ML).



