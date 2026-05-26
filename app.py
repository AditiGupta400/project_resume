import streamlit as st

from utils import extract_text, extract_skills
from projects import recommend_projects

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Resume Project Recommender",
    page_icon="📄",
    layout="wide"
)

# ---------------- HEADER ---------------- #
st.title("📄 AI Resume Project Recommender")
st.write("Upload your resume and get AI-based project suggestions + skill analysis.")

# ---------------- SKILL LIST ---------------- #
skills_list = [
    "python", "sql", "power bi", "excel",
    "machine learning", "data analysis",
    "pandas", "numpy", "nlp", "statistics",
    "deep learning", "tableau"
]

# ---------------- UPLOAD FILE ---------------- #
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:

    # Extract resume text
    resume_text = extract_text(uploaded_file)

    st.subheader("📄 Resume Preview")
    st.write(resume_text[:1200])

    # Extract skills
    skills = extract_skills(resume_text, skills_list)

    st.subheader("🧠 Detected Skills")
    st.write(skills)

    # Generate projects (ONLY ONCE)
    projects = recommend_projects(skills)

    st.subheader("🚀 Recommended Industry Projects")

    for p in projects:

        st.markdown(f"""
### 📌 {p['project']}

🧠 **Skills Used:** {", ".join(p['skills'])}

📄 **Description:**  
{p['desc']}

---
""")
