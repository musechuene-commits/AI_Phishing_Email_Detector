# 🛡️ AI-Powered Phishing Email Detector

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Project-orange)
![GitHub Actions](https://github.com/musechuene-commits/AI_Phishing_Email_Detector/actions/workflows/python-ci.yml/badge.svg)

---

# 📌 Overview

AI-Powered Phishing Email Detector is a cybersecurity project developed in Python to analyze email content and identify potential phishing attacks using both rule-based detection and machine learning classification.

The application scans email text for suspicious phishing indicators such as:

- Social engineering language
- Urgent security warnings
- Suspicious URLs
- Unsafe domains
- Password reset scams
- Fake banking notifications

The project combines:

- Rule-based threat analysis
- AI / Machine Learning phishing classification
- Streamlit web dashboard visualization
- CI/CD automation with GitHub Actions
- Automated security scanning

This project simulates a lightweight SOC-style phishing detection tool used in cybersecurity and DevSecOps environments.

---

# 🚀 Features

## 🔍 Rule-Based Detection

- Phishing keyword detection
- URL analysis
- Suspicious domain detection
- HTTP link detection
- Threat scoring system
- Detection reasoning output

---

## 🤖 Machine Learning Classification

- Natural Language Processing (NLP)
- Scikit-learn integration
- Naive Bayes classification
- AI confidence scoring
- Trained phishing dataset model

---

## 📊 Streamlit Dashboard

- Interactive web interface
- Real-time phishing analysis
- Threat visualization
- Confidence score display
- User-friendly scanning workflow

---

## ⚙️ DevOps & DevSecOps Features

- GitHub Actions CI/CD pipeline
- Automated Python syntax validation
- Automated testing with pytest
- Code quality scanning using flake8
- Security scanning using Bandit
- Docker container support

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application dashboard |
| Scikit-learn | Machine learning classification |
| Pandas | Data handling |
| GitHub Actions | CI/CD automation |
| Pytest | Automated testing |
| Flake8 | Code quality scanning |
| Bandit | Security scanning |
| Docker | Containerization |

---

# 📂 Project Structure

```text
AI_Phishing_Email_Detector/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── screenshots/
│
├── tests/
│   └── test_detector.py
│
├── app.py
├── ai_detector.py
├── detector.py
├── train_model.py
├── phishing_model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
└── dataset.csv
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/musechuene-commits/AI_Phishing_Email_Detector.git
```

---

## 2️⃣ Navigate Into Project

```bash
cd AI_Phishing_Email_Detector
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

# 🧪 Automated Testing

Run pytest tests:

```bash
pytest
```

---

# 🔎 Code Quality Scanning

Run flake8 scan:

```bash
flake8 . --exclude=.venv,venv,__pycache__ --max-line-length=120
```

---

# 🔐 Security Scanning

Run Bandit security scan:

```bash
bandit -r .
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t phishing-detector .
```

---

## Run Docker Container

```bash
docker run -p 8501:8501 phishing-detector
```

---

## Access Application

Open browser:

```text
http://localhost:8501
```

---

# 📸 Screenshots

## Dashboard Interface

_Add screenshot here_

---

## Safe Email Detection

_Add screenshot here_

---

## Phishing Email Detection

_Add screenshot here_

---

## Uploaded Email Scan

_Add screenshot here_

---

# 🔄 CI/CD Pipeline

This project includes a GitHub Actions CI/CD pipeline that automatically:

- Installs dependencies
- Validates Python syntax
- Runs automated tests
- Performs code quality checks
- Executes security scanning

Workflow file:

```text
.github/workflows/python-ci.yml
```

---

# 🎯 Future Improvements

- Email attachment analysis
- OCR scanning for phishing PDFs
- Real-time email API integration
- Advanced NLP models
- Threat intelligence integration
- SIEM integration
- Azure deployment
- Kubernetes deployment
- Secrets scanning with Gitleaks

---

# 👨‍💻 Author

## Musa Chuene

- 💼 IT Support | Cybersecurity | DevSecOps Enthusiast
- 🔗 GitHub: https://github.com/musechuene-commits
- 🔗 LinkedIn: https://linkedin.com/in/musa-chuene-57a4461a8

---

# ⚠️ Disclaimer

This project was developed strictly for educational, research, and portfolio purposes.

The application is intended to simulate phishing detection workflows commonly used in cybersecurity environments and should not be used maliciously.

---

# ⭐ Support

If you found this project useful:

- Star the repository
- Fork the project
- Share feedback
- Connect on LinkedIn