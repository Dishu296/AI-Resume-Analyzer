import streamlit as st
import PyPDF2
import docx
import re
import spacy
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_sm")

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="wide")

st.title("🧠 AI Resume Analyzer")
st.write("Analyze your resume and get your ATS compatibility score!")

# Upload section
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])

job_desc = st.text_area("💼 Paste the Job Description", height=150)

if uploaded_file is not None:
    # Extract text
    text = ""
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text

    st.subheader("📊 Resume Summary")
    st.write(text[:1000] + "..." if len(text) > 1000 else text)

    if st.button("🔍 Analyze Resume"):
        jd_doc = nlp(job_desc)
        resume_doc = nlp(text)

        # Extract nouns and proper nouns as potential keywords
        jd_keywords = [token.text.lower() for token in jd_doc if token.pos_ in ["NOUN", "PROPN"]]
        resume_keywords = [token.text.lower() for token in resume_doc if token.pos_ in ["NOUN", "PROPN"]]

        jd_keywords = list(set(jd_keywords))
        resume_keywords = list(set(resume_keywords))

        matched = [word for word in jd_keywords if word in resume_keywords]
        score = round((len(matched) / len(jd_keywords)) * 100, 2) if len(jd_keywords) > 0 else 0

        st.success(f"✅ Your Resume Score: {score}/100")
        st.write("### 🔑 Matched Keywords:")
        st.write(", ".join(matched) if matched else "No matching keywords found.")

        # Visualization
        if matched:
            wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(matched))
            st.pyplot(plt.imshow(wc, interpolation="bilinear"))
            plt.axis("off")

        st.write("### 📝 Suggestions:")
        if score < 60:
            st.warning("Add more relevant keywords from the job description to improve your ATS score.")
        elif score < 85:
            st.info("Good resume! Add a few more technical terms for a stronger match.")
        else:
            st.success("Excellent! Your resume is highly optimized for this job.")
