🧠 AI Resume Analyzer

An intelligent Streamlit-based app that analyzes resumes (PDF/DOCX) using NLP and ML to extract key information, score skills, and provide improvement insights.

🚀 Project Overview

The AI Resume Analyzer helps users evaluate their resumes using natural language processing and machine learning.
It extracts text, identifies skills, experience, and education sections, compares them to job descriptions, and provides suggestions for improvement.

This can be helpful for:

Students preparing resumes for internships or placements

Recruiters screening resumes efficiently

Job seekers optimizing their resumes for specific roles

🧩 Features

✅ Upload resumes in PDF or DOCX format
✅ Extract and analyze key resume sections (Skills, Education, Experience)
✅ Skill matching with job descriptions
✅ Generate summary insights and keyword suggestions
✅ Visualize skill frequency with a WordCloud
✅ Clean and modern Streamlit UI

🧠 Tech Stack
Category	Technology
Frontend	Streamlit
Backend / ML	Python, spaCy, NLTK, scikit-learn
Libraries	PyPDF2, python-docx, pandas, matplotlib, wordcloud
NLP Model	spaCy en_core_web_sm
📦 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Download spaCy model
python -m spacy download en_core_web_sm

4️⃣ Run the app
streamlit run app.py


The app will launch at 👉 http://localhost:8501

📂 Project Structure
AI-Resume-Analyzer/
│
├── app.py                 # Main Streamlit app
├── resume_parser.py       # Text extraction and NLP functions
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── data/                  # Sample resumes
├── assets/                # Images, logos, visuals
