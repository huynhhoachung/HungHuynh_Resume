from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir /"resume.png"#/ "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hung Huynh (Clark Huynh)"
PAGE_ICON = ":wave:"
NAME = "Hung Huynh"
DESCRIPTION = """
Data Analyst with 1.5 years of experience in requirement analysis, data modeling, statistical analyzing with data driven mindset. Adept at driving business
performance through strategic action plans.
"""
EMAIL = "hoachung.huynh@gmail.com"
PHONE_NUMBER = "0937861237"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/hung-huynh-71808b1ba",
    "GitHub": "https://github.com/huynhhoachung",
    "Kaggle":"https://www.kaggle.com/clarkhuynh"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 My personal project": "https://youtu.be/3egaMfE9388",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([0.35, 0.65], gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📞", PHONE_NUMBER)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA),gap = 'small')
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1.5 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of Machine Learning.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
"""
- 🖥️ Operating system: MacOS, Windows, Linux.
- 👩‍💻 Programming languages: C# and Python.
- 🗄️ Database querying: SQL, MongoDB.
- 📊 Data Visulization: Matplotlib, Seaborn, Plotly, Redash, Mixpanel, Kibana, Streamlit.
- 📚 Libraries: Pandas, Numpy, Scikit Learn, OpenCV.
- 🛠️ Working tools: Jira, Slack, Notion, Github, Flask.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Fresher Data Analyst | FIKA SOCIAL VIET NAM**")
st.write("October 2022 - May 2023")
st.write(
    """
- ► Assist in the development of data models and statistical analysis to identify trends and insights which help raised users retention rate up to 80% for D1 and 40% for D30.
- ► Create data visualizations and dashboards with Streamlit, Redash(Open source), Elastic Search - Kibana and Mixpanel.
- ► Build API bot using Flask and Webhook for monitoring purposes.
- ► Build data-mart for data tracking using Mixpanel.
- ► Collaborate with cross-functional teams to give data-driven decision-making.
- ► Evaluate product features applying rules-based and AI models.
- ► Working closely with C-Suite to provide funding data.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**CTO Assistant | FIKA SOCIAL VIET NAM**")
st.write("October 2021 - September 2022")
st.write(
    """
- ► Provide business and administrative support to the CTO.
- ► Act as a primary point of contact for all internal and external
communications with the CTO.
- ► Arrange meeting agendas, take notes & actions when needed, help
the team unpick problems, and keep them aligned and
accountable.
- ► Research and provide AI-relevant solutions together with CTO.
- ► Extract, visualize data and create report to evaluate product
directional decisions.
- ► PO of 16 personalities test feature of Fika.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
