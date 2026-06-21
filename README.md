# TalentMatch AI 🚀

TalentMatch AI is a Machine Learning-based Resume Screening and Candidate Ranking System designed to simplify the recruitment process. The application analyzes resumes, classifies candidate profiles, extracts relevant skills, and ranks applicants against job requirements using NLP and similarity-based matching techniques.

Built with Python, Scikit-learn, and Streamlit, TalentMatch AI helps recruiters quickly identify the most suitable candidates while reducing manual screening effort.

---

## ✨ Features

- 📄 Resume Classification using Machine Learning
- 🧠 Resume Encoding and Vectorization
- 🛠 Automatic Skill Extraction
- 🎯 Candidate-Job Matching
- 📊 Candidate Ranking based on Similarity Scores
- 🌐 Interactive Streamlit Dashboard

---

## 📂 Project Structure

```text
FUTURE_ML_03/
│
├── data/
│   ├── jobs.csv
│   ├── resumes.csv
│   └── processed_resumes.csv
│
├── models/
│   ├── resume_classifier.pkl
│   ├── resume_encoder.pkl
│   ├── resume_vectorizer.pkl
│   └── resume_vectors.pkl
│
├── scripts/
│   ├── preprocess.py
│   ├── train_category_model.py
│   └── train_resume_encoder.py
│
├── utils/
│   ├── candidate_ranker.py
│   ├── predict.py
│   └── skill_extractor.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **NLTK**
- **Streamlit**

---

## 🔄 Workflow

1. Preprocess resume and job datasets.
2. Train the resume classification model.
3. Generate resume embeddings and vectors.
4. Extract candidate skills.
5. Compare resumes with job requirements.
6. Rank candidates based on similarity scores.
7. Display results through the Streamlit dashboard.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/TalentMatch-AI.git
cd TalentMatch-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Train Models

Preprocess the dataset:

```bash
python scripts/preprocess.py
```

Train the classification model:

```bash
python scripts/train_category_model.py
```

Train the resume encoder:

```bash
python scripts/train_resume_encoder.py
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

---

## 📈 How Candidate Ranking Works

The system converts resumes and job descriptions into numerical vectors using NLP techniques. Cosine Similarity is then used to measure how closely a candidate's profile matches a job requirement. Candidates are ranked according to their matching scores, allowing recruiters to identify top applicants quickly.

Example:

```text
Candidate A : 92.4%
Candidate B : 87.8%
Candidate C : 81.3%
```

---

## 🔮 Future Enhancements

- Resume PDF Upload Support
- Skill Gap Analysis
- AI-Powered Resume Feedback
- Interview Question Recommendations
- Recruiter Analytics Dashboard
- LLM-Based Candidate Summarization

---

## 👨‍💻 Author

**Lohitha Revu**  
