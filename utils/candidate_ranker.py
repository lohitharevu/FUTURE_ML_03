import pandas as pd
import joblib

from sklearn.metrics.pairwise import cosine_similarity
resume_encoder = joblib.load(
    "models/resume_encoder.pkl"
)

resume_vectors = joblib.load(
    "models/resume_vectors.pkl"
)

resumes_df = pd.read_csv(
    "data/processed_resumes.csv"
)
def get_recommendation(score):

    if score >= 85:
        return "Highly Recommended"

    elif score >= 70:
        return "Recommended"

    elif score >= 50:
        return "Consider for Review"

    else:
        return "Not Recommended"

def rank_candidates(
    job_description,
    top_n=10
):

    # Convert Job Description into Vector

    job_vector = resume_encoder.transform(
        [job_description]
    )

    # Calculate Similarity

    similarity_scores = cosine_similarity(
        job_vector,
        resume_vectors
    )[0]

    results = []

    for idx, score in enumerate(
        similarity_scores
    ):

        score = round(
            score * 100,
            2
        )

        results.append({

            "Candidate ID":
            resumes_df.iloc[idx]["ID"],

            "Category":
            resumes_df.iloc[idx]["Category"],

            "Match Score":
            score,

            "Recommendation":
            get_recommendation(score)
        })

    ranking_df = pd.DataFrame(
        results
    )

    ranking_df = ranking_df.sort_values(
        by="Match Score",
        ascending=False
    )

    ranking_df = ranking_df.reset_index(
        drop=True
    )

    return ranking_df.head(top_n)

def get_best_candidate(
    job_description
):

    ranking = rank_candidates(
        job_description,
        top_n=1
    )

    return ranking.iloc[0]

if __name__ == "__main__":

    sample_job = """
    Looking for a Machine Learning Engineer
    with Python, SQL, AWS, Docker,
    TensorFlow and Deep Learning experience.
    """

    top_candidates = rank_candidates(
        sample_job,
        top_n=5
    )

    print("\nTOP CANDIDATES\n")

    print(top_candidates)

    print("\nBEST CANDIDATE\n")

    print(
        get_best_candidate(
            sample_job
        )
    )