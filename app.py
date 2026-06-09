import streamlit as st
import pandas as pd
import plotly.express as px

from utils.predict import analyze_resume
from utils.candidate_ranker import rank_candidates

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="TalentMatch AI",
    page_icon="🎯",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.metric-card {
    padding: 15px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
}

.big-font {
    font-size: 22px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.title("🎯 TalentMatch AI")

st.caption(
    "AI-Powered Resume Screening & Candidate Ranking Platform"
)

st.divider()

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(

    "Select Module",

    [
        "Resume Analyzer",
        "Candidate Ranking"
    ]
)

# ==================================================
# RESUME ANALYZER
# ==================================================

if page == "Resume Analyzer":

    st.header("📄 Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:

        job_description = st.text_area(

            "Job Description",

            height=300,

            placeholder="""
Looking for Machine Learning Engineer
with Python, SQL, AWS,
Docker and TensorFlow.
"""
        )

    with col2:

        resume_text = st.text_area(

            "Resume",

            height=300,

            placeholder="""
Machine Learning Engineer
with Python, SQL,
Docker and TensorFlow.
"""
        )

    if st.button("🚀 Analyze Resume"):

        if not job_description or not resume_text:

            st.warning(
                "Please enter both fields."
            )

        else:

            result = analyze_resume(

                resume_text,

                job_description
            )

            st.success(
                "Analysis Completed"
            )

            # ==========================
            # KPI CARDS
            # ==========================

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "🎯 Match Score",
                f"{result['match_score']}%"
            )

            c2.metric(
                "📚 Skill Match",
                f"{result['skill_score']}%"
            )

            c3.metric(
                "🏆 Recommendation",
                result['recommendation']
            )

            st.divider()

            # ==========================
            # SKILLS
            # ==========================

            left, right = st.columns(2)

            with left:

                st.subheader(
                    "✅ Matched Skills"
                )

                if result["matched_skills"]:

                    for skill in result[
                        "matched_skills"
                    ]:

                        st.success(skill)

                else:

                    st.info(
                        "No matched skills"
                    )

            with right:

                st.subheader(
                    "❌ Missing Skills"
                )

                if result["missing_skills"]:

                    for skill in result[
                        "missing_skills"
                    ]:

                        st.error(skill)

                else:

                    st.success(
                        "No missing skills"
                    )

            st.divider()

            # ==========================
            # PIE CHART
            # ==========================

            matched = len(
                result["matched_skills"]
            )

            missing = len(
                result["missing_skills"]
            )

            chart_df = pd.DataFrame({

                "Type": [
                    "Matched",
                    "Missing"
                ],

                "Count": [
                    matched,
                    missing
                ]
            })

            fig = px.pie(

                chart_df,

                values="Count",

                names="Type",

                title="Skill Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

# ==================================================
# CANDIDATE RANKING
# ==================================================

elif page == "Candidate Ranking":

    st.header(
        "🏆 Candidate Ranking System"
    )

    job_description = st.text_area(

        "Enter Job Description",

        height=250
    )

    top_n = st.slider(

        "Top Candidates",

        5,
        50,
        10
    )

    if st.button(
        "Generate Ranking"
    ):

        if not job_description:

            st.warning(
                "Enter Job Description"
            )

        else:

            ranking_df = rank_candidates(

                job_description,

                top_n
            )

            st.success(
                "Ranking Generated"
            )

            st.dataframe(

                ranking_df,

                use_container_width=True
            )

            st.divider()

            st.subheader(
                "📊 Match Score Distribution"
            )

            fig = px.bar(

                ranking_df,

                x="Candidate ID",

                y="Match Score",

                color="Match Score",

                title="Top Candidates"
            )

            st.plotly_chart(

                fig,

                use_container_width=True
            )

            st.subheader(
                "🥇 Best Candidate"
            )

            best = ranking_df.iloc[0]

            st.success(
                f"""
Candidate ID: {best['Candidate ID']}

Category: {best['Category']}

Match Score: {best['Match Score']}%

Recommendation: {best['Recommendation']}
"""
            )

# ==================================================
# MODEL INFORMATION
# ==================================================

st.divider()

st.markdown("""
### 📌 Model Information & Disclaimer

**TalentMatch AI** uses Machine Learning and Natural Language Processing (NLP)
techniques to analyze resumes, extract skills, calculate job-fit scores,
and rank candidates based on similarity and skill matching.

⚠️ **Important Note**

- Results are generated using models trained on the provided resume dataset.
- Match scores, rankings, and recommendations depend on the quality, size,
  diversity, and distribution of the training data.
- Predictions may vary when evaluated on different resumes, job descriptions,
  industries, or real-world hiring scenarios.
- This platform is designed as an intelligent decision-support tool and
  should not be considered a replacement for human recruiter evaluation.
- Actual hiring decisions should always involve manual review and
  professional assessment.

### 📊 System Components

✅ Resume Category Classification

✅ Skill Extraction Engine

✅ Resume-to-Job Matching

✅ Candidate Ranking

✅ Skill Gap Analysis

✅ Hiring Recommendation System

---
""")

# ==================================================
# FOOTER
# ==================================================

st.caption(
    "TalentMatch AI • Resume Screening • Candidate Ranking • Skill Gap Analysis • Powered by Machine Learning & NLP"
)