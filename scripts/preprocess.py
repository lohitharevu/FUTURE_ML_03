import pandas as pd
import re

# ==========================================
# TEXT CLEANING FUNCTION
# ==========================================

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'www\S+', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# ==========================================
# LOAD RESUME DATASET
# ==========================================

df = pd.read_csv("resumes.csv")

print("Original Shape:", df.shape)

# Keep only required columns
df = df[["ID", "Resume_str", "Category"]]

# Remove missing values
df = df.dropna()

# Clean resume text
df["clean_resume"] = df["Resume_str"].apply(clean_text)

# Keep final columns
processed_df = df[
    [
        "ID",
        "clean_resume",
        "Category"
    ]
]

# Save file
processed_df.to_csv(
    "processed_resumes.csv",
    index=False
)

print("✅ processed_resumes.csv created successfully")
print("Shape:", processed_df.shape)

print("\nPreview:")
print(processed_df.head())