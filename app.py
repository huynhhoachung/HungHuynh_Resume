from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir /"resume_pic.png"#/ "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV |Hung Huynh(Clark Huynh)"
PAGE_ICON = ":wave:"
NAME = "Hung Huynh (Clark Huynh)"
DESCRIPTION = """
Data Analyst with 1.5 years of experience in requirement analysis, data modeling, statistical analyzing with deep understanding in machine learning, deep learning. Adept at driving business
performance through strategic action plans.
"""
EMAIL = "hoachung.huynh@gmail.com"
PHONE_NUMBER = "0937861237"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/hung-huynh-71808b1ba",
    "GitHub": "https://github.com/huynhhoachung"
}
PROJECTS = {
    "🏆 Fake New Detection Models Evaluation": "https://github.com/huynhhoachung/Fake_New_Detection_Evaluation",
    "🏆 Country Statistics EDA": "https://github.com/huynhhoachung/Country_Statistics_EDA",
    #"🏆 Real-time Object Detection with Tensorflow": "https://github.com/huynhhoachung/Country_Statistics_EDA",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([0.45, 0.55], gap="small")
with col1:
    st.image(profile_pic, width = 270 , output_format='png')

with col2:
    st.title(NAME)
    st.write("📫", EMAIL)
    st.write("📞", PHONE_NUMBER)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )


# # --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns([1,1,1,1],gap = 'small')
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")
# st.write("---")

# --- Description ---
#st.subheader(f":white[Short introduction]")
st.write(DESCRIPTION)
st.write("---")
#st.write('\n')


# --- EXPERIENCE & QUALIFICATIONS ---
#st.write('\n')
st.subheader(f"Experience & Qualifications")
st.write(
    """
- ✔️ 1.5 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and SQL/NoSQL
- ✔️ Good understanding of Machine Learning.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader(f"Hard Skills")
st.write(
"""
- 🖥️ Operating system: MacOS, Windows, Linux.
- 👩‍💻 Programming languages: C# and Python.
- 🗄️ Database querying: SQL, MongoDB.
- 📊 Data Visulization: Matplotlib, Seaborn, Plotly, Wordcloud, Redash, Mixpanel, Kibana, Streamlit.
- 📚 Libraries: Pandas, Numpy, Scikit Learn, OpenCV.
- 🛠️ Working tools: Jira, Slack, Notion, Github, Flask.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader(f"Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | FIKA SOCIAL VIET NAM**")
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
- ► Research and provide AI-relevant solutions together with CTO.
- ► Extract, visualize data and create report to evaluate product
directional decisions.
- ► PO of 16 personalities test feature of Fika.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader(f"Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
