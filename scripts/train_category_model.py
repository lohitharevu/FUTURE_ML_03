import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report
)

df = pd.read_csv("resumes.csv")

# Keep only required columns
df = df[["Resume_str", "Category"]]

# Remove missing values
df = df.dropna()

print("Dataset Shape:", df.shape)

X = df["Resume_str"]
y = df["Category"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000,
    ngram_range=(1, 2)
)

X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = LogisticRegression(
    max_iter=2000,
    random_state=42
)

print("\nTraining model...\n")

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("=" * 50)
print("MODEL ACCURACY")
print("=" * 50)

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred
    )
)

joblib.dump(
    model,
    "resume_classifier.pkl"
)

joblib.dump(
    vectorizer,
    "resume_vectorizer.pkl"
)

print("\n✅ resume_classifier.pkl saved")
print("✅ resume_vectorizer.pkl saved")