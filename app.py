

import streamlit as st
import pdfplumber


# --------------------------------
# TITLE
# --------------------------------

st.title(
    "AI Career Gap Recovery Assistant"
)


# --------------------------------
# PDF TEXT EXTRACTION FUNCTION
# --------------------------------

def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted

    return text


# --------------------------------
# FILE UPLOAD
# --------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


# --------------------------------
# PROCESS RESUME
# --------------------------------

if uploaded_file:

    st.success(
        "Resume Uploaded Successfully"
    )

    # Extract Resume Text
    resume_text = extract_text_from_pdf(
        uploaded_file
    )

    # Show Resume Text
    st.subheader(
        "Resume Text"
    )

    st.write(
        resume_text
    )


    # --------------------------------
    # REQUIRED SKILLS
    # --------------------------------

    required_skills = [

        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Statistics",
        "Power BI",
        "Generative AI"
    ]


    # --------------------------------
    # DETECTED SKILLS
    # --------------------------------

    found_skills = []

    for skill in required_skills:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)


    st.subheader(
        "Detected Skills"
    )

    st.write(
        found_skills
    )


    # --------------------------------
    # MISSING SKILLS
    # --------------------------------

    missing_skills = []

    for skill in required_skills:

        if skill not in found_skills:

            missing_skills.append(skill)


    st.subheader(
        "Missing Skills"
    )

    st.write(
        missing_skills
    )


    # --------------------------------
    # PROFILE SCORE
    # --------------------------------

    total_skills = len(required_skills)

    detected_count = len(found_skills)

    score = (
        detected_count / total_skills
    ) * 100


    st.subheader(
        "Profile Match Score"
    )

    st.write(
        f"{score:.2f}%"
    )


    # --------------------------------
    # CAREER SUGGESTIONS
    # --------------------------------

    st.subheader(
        "Career Suggestions"
    )

    if score >= 80:

        st.success(
            "Strong profile for Data Scientist roles"
        )

    elif score >= 60:

        st.warning(
            "Good profile. Improve missing skills."
        )

    else:

        st.error(
            "Need more skills and projects."
        )