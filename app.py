from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = " CV | Kartik Gupta"
#PAGE_ICON = "/assets/profile-pic.png"
NAME = "Kartik Gupta"
DESCRIPTION = """
Tech Enthusiast | Software Developer 
Android | Python | DSA | Web Dev
"""
EMAIL = "guptakartik851@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/kartik-gupta-15792a174/",
    "GitHub": "https://github.com/kartik2629",
    "Leetcode": "https://leetcode.com/u/kartik851/",
    "Twitter":"https://x.com/Kartik26Gupta?s=09",
}
PROJECTS = {
    "🏆 Chatalytics - WhatsApp Chat Analyzer using Data Science": "https://github.com/kartik2629/Chatalytics",
    "🏆 Daily News Shots - News Application using Android with NewsAPI": "https://github.com/kartik2629/News-App",
    "🏆 ATS Resume Parser - Resume Parser and Extractor using Data Science": "https://github.com/kartik2629/Resume-Parser",
    "🏆 WeatherApp - Simple weather application in HTML CSS with weatherAPI": "https://github.com/kartik2629/Weather-App",
    "🏆 PassMan - Password Manager using react and vite":"https://github.com/kartik2629/PassManager-using-React-Vite",
    "🏆 Healthify - A complete medicare solution Android App":"https://github.com/kartik2629/Healthify/tree/master",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon="icon.png")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

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
st.write("""

Final year student proficient in Python, Android development (Kotlin), HTML, CSS, data science, and DBMS. Seeking entry-level
role to apply academic knowledge and gain industry experience.
""")


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write("---")



# --- EDUCATION ---
st.write('\n')
st.subheader("🏫 Education")
st.write("---")

# --- EDU 1
st.write("📚", "**Integrated IMCA | Parul University® , Vadodara , Gujarat**")
st.write("- 08/2021 - 04/2025")
st.write("- CGPA : 8.95/10")

# --- EDU 1
st.write("📚", """**Class 12 (Senior Secondary Examination) | Smt. Kamala Saklecha Gyan Mandir**""")
st.write("- 04/2020 - 07/2021")
st.write("- Percentage: 92.2%")


# --- SKILLS ---
st.write('\n')
st.subheader("🎓 Skills")
st.write("---")
st.write(
    """
- 🤖 Programming: C | Python | Java | Kotlin | JavaScript (JS) | SQL
- 🌐 Web Development: HTML | CSS | ASP.NET
- 📊 Framework: Android | Streamlit | Data Science & Visualisation
- 🗃️ Databases: MySQL | MongoDB | Oracle Express
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("👨🏻‍💻 Work Experience - Internships/Trainings")
st.write("---")

# --- JOB 1
st.write("🚧", "**Android Development | Bharat Intern**")
st.write("07/2023 - 08/2023")
st.write(
    """
- ► Developed and implemented Android applications according to client requirements.
- ► Participated in all stages of the software development lifecycle.
- ► Implemented key features resulting in improved app performance.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Industrial Trainee | Intel®**")
st.write("06/2023 - 09/2023")
st.write(
    """
- ► Developed and tested ATM FSM controller on VLDC platform.
- ► Collaborated with team to meet project requirements.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("🗂️ Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


st.write('\n')
st.subheader("🏆 Awards and Certificates")
st.write("---")
st.write(
    """
- ► Consistently achieved top academic rankings in all completed semesters.
- ► Completed Spoken Tutorial Certificates on C , Python , Android , PHP , SQL etc.. 
"""
)
