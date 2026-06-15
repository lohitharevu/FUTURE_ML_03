import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("processed_resumes.csv")

df = df.dropna(subset=["clean_resume"])

print("Total Resumes:", len(df))

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=15000,
    ngram_range=(1, 2)
)

resume_vectors = vectorizer.fit_transform(
    df["clean_resume"]
)

joblib.dump(
    vectorizer,
    "resume_encoder.pkl"
)

joblib.dump(
    resume_vectors,
    "resume_vectors.pkl"
)

print("✅ resume_encoder.pkl saved")
print("✅ resume_vectors.pkl saved")

print("Vector Shape:", resume_vectors.shape)