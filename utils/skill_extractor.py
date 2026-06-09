import re

# =====================================================
# MASTER SKILL DATABASE
# =====================================================

SKILLS_DB = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "r",
    "go",
    "rust",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",
    "sqlite",

    # Data Science
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "data visualization",
    "statistics",
    "predictive analytics",

    # AI / ML
    "tensorflow",
    "pytorch",
    "keras",
    "opencv",
    "nlp",
    "computer vision",
    "generative ai",
    "llm",
    "transformers",

    # Cloud
    "aws",
    "azure",
    "gcp",
    "cloud computing",

    # DevOps
    "docker",
    "kubernetes",
    "jenkins",
    "git",
    "github",
    "gitlab",
    "ci/cd",

    # BI Tools
    "power bi",
    "tableau",
    "excel",

    # Web Development
    "html",
    "css",
    "bootstrap",
    "react",
    "angular",
    "vue",
    "nodejs",
    "express",
    "flask",
    "django",
    "fastapi",

    # Mobile Development
    "android",
    "flutter",
    "react native",

    # Cybersecurity
    "network security",
    "ethical hacking",
    "penetration testing",
    "cybersecurity",

    # Software Engineering
    "oop",
    "data structures",
    "algorithms",
    "system design",

    # Soft Skills
    "leadership",
    "communication",
    "teamwork",
    "problem solving",
    "project management",
    "critical thinking"
]


# =====================================================
# CLEAN TEXT
# =====================================================

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r'[^a-z0-9+#.\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# =====================================================
# EXTRACT SKILLS
# =====================================================

def extract_skills(text):

    text = clean_text(text)

    found_skills = set()

    for skill in SKILLS_DB:

        skill_pattern = r'\b' + re.escape(skill.lower()) + r'\b'

        if re.search(skill_pattern, text):
            found_skills.add(skill)

    return sorted(list(found_skills))


# =====================================================
# SKILL MATCH %
# =====================================================

def calculate_skill_match(
    resume_skills,
    job_skills
):

    if len(job_skills) == 0:
        return 0

    matched = set(resume_skills).intersection(
        set(job_skills)
    )

    score = (
        len(matched)
        / len(job_skills)
    ) * 100

    return round(score, 2)


# =====================================================
# MISSING SKILLS
# =====================================================

def get_missing_skills(
    resume_skills,
    job_skills
):

    return sorted(
        list(
            set(job_skills)
            - set(resume_skills)
        )
    )


# =====================================================
# MATCHED SKILLS
# =====================================================

def get_matched_skills(
    resume_skills,
    job_skills
):

    return sorted(
        list(
            set(job_skills)
            .intersection(
                set(resume_skills)
            )
        )
    )


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    resume = """
    Machine Learning Engineer with Python,
    SQL, AWS, Docker, TensorFlow,
    Git and Power BI experience.
    """

    job = """
    Looking for Machine Learning Engineer
    with Python, SQL, AWS,
    TensorFlow and Kubernetes.
    """

    resume_skills = extract_skills(resume)

    job_skills = extract_skills(job)

    print("Resume Skills:")
    print(resume_skills)

    print("\nJob Skills:")
    print(job_skills)

    print("\nMatched Skills:")
    print(
        get_matched_skills(
            resume_skills,
            job_skills
        )
    )

    print("\nMissing Skills:")
    print(
        get_missing_skills(
            resume_skills,
            job_skills
        )
    )

    print("\nSkill Match Score:")
    print(
        calculate_skill_match(
            resume_skills,
            job_skills
        ),
        "%"
    )