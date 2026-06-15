import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.skill_extractor import extract_skills

def get_recommendation(score):

    if score >= 85:
        return "Highly Recommended"

    elif score >= 70:
        return "Recommended"

    elif score >= 50:
        return "Consider for Review"

    return "Not Recommended"

def category_bonus(resume_category, job_description):

    resume_category = str(resume_category).lower()
    job_description = str(job_description).lower()

    keywords = {
        "data science": [
            "machine learning",
            "data scientist",
            "ai",
            "analytics"
        ],

        "java developer": [
            "java",
            "spring",
            "backend"
        ],

        "devops engineer": [
            "docker",
            "kubernetes",
            "aws"
        ],

        "testing": [
            "testing",
            "qa",
            "automation"
        ]
    }

    for category, words in keywords.items():

        if category in resume_category:

            for word in words:

                if word in job_description:
                    return 15

    return 0

def analyze_resume(
    resume_text,
    job_description,
    resume_category="Unknown"
):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = list(
        set(resume_skills).intersection(job_skills)
    )

    missing_skills = list(
        set(job_skills) - set(resume_skills)
    )

    # Skill Match Score
    if len(job_skills) > 0:
        skill_score = (
            len(matched_skills)
            / len(job_skills)
        ) * 100
    else:
        skill_score = 0

    # TF-IDF Similarity
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([
        resume_text,
        job_description
    ])

    similarity_score = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0] * 100

    # Category Match Bonus
    bonus = category_bonus(
        resume_category,
        job_description
    )

    # Weighted Score
    final_score = (
        (0.6 * skill_score)
        + (0.4 * similarity_score)
        + bonus
    )

    final_score = min(
        round(final_score, 2),
        100
    )

    recommendation = get_recommendation(
        final_score
    )

    strengths = matched_skills[:5]

    weaknesses = missing_skills[:5]

    return {

        "match_score": final_score,

        "skill_score": round(
            skill_score,
            2
        ),

        "similarity_score": round(
            similarity_score,
            2
        ),

        "matched_skills": sorted(
            matched_skills
        ),

        "missing_skills": sorted(
            missing_skills
        ),

        "strengths": strengths,

        "weaknesses": weaknesses,

        "recommendation": recommendation
    }

def rank_candidates(
    resumes_df,
    job_description
):

    rankings = []

    for _, row in resumes_df.iterrows():

        result = analyze_resume(
            row["clean_resume"],
            job_description,
            row["Category"]
        )

        rankings.append({

            "Candidate ID":
            row["ID"],

            "Category":
            row["Category"],

            "Match Score":
            result["match_score"],

            "Recommendation":
            result["recommendation"]
        })

    ranked = pd.DataFrame(rankings)

    ranked = ranked.sort_values(
        by="Match Score",
        ascending=False
    )

    return ranked.reset_index(
        drop=True
    )

if __name__ == "__main__":

    job = """
    Looking for a Machine Learning Engineer
    with Python, SQL, AWS, Docker,
    TensorFlow and Machine Learning.
    """

    resume = """
    Machine Learning Engineer with Python,
    SQL, Docker, TensorFlow and AI projects.
    """

    result = analyze_resume(
        resume,
        job,
        "Data Science"
    )

    print(result)