# AI-Powered Phishing Email Detector

## Overview

AI-Powered Phishing Email Detector is a Python-based cybersecurity tool designed to analyze email text and identify potential phishing attempts.

The project uses rule-based threat detection to inspect suspicious keywords, URLs, insecure links, and social engineering indicators. It then generates a threat score and provides a clear security verdict.

This project simulates how a basic SOC or security support tool can assist analysts in identifying suspicious email content.

---

## Key Features

- Detects phishing-related keywords
- Identifies suspicious URLs
- Flags insecure HTTP links
- Detects suspicious top-level domains
- Generates a phishing threat score
- Provides a clear verdict: Low Risk, Suspicious, or High Risk Phishing
- Displays reasons for the detection result
- Beginner-friendly cybersecurity automation project

---

## Technologies Used

- Python
- Regular Expressions
- Threat Scoring Logic
- Cybersecurity Detection Rules

---

## Project Structure

```text
AI_Phishing_Email_Detector/
│
├── app.py
├── detector.py
├── phishing_samples.txt
├── requirements.txt
├── README.md
└── screenshots/

How It Works

The detector checks an email message for common phishing indicators such as:

Urgent language
Account suspension warnings
Password reset requests
Fake banking messages
Suspicious links
Insecure HTTP URLs
Suspicious domains such as .xyz, .tk, .top, and .click

Each indicator increases the threat score. Based on the final score, the tool returns a risk verdict.

Example Phishing Email
Urgent! Your bank account has been suspended. Click here to verify your account immediately: http://secure-bank-login.xyz

Example Output
Threat Score: 100%
Verdict: HIGH RISK PHISHING

Reasons:
- Suspicious keyword detected: 'urgent'
- Suspicious keyword detected: 'bank account'
- Suspicious keyword detected: 'click here'
- URL detected: http://secure-bank-login.xyz
- Suspicious domain detected: .xyz
- Insecure HTTP link detected

How to Run

Clone the repository:

git clone https://github.com/musechuene-commits/Syntecxhub_AI_Phishing_Email_Detector.git

Open the project folder:

cd AI_Phishing_Email_Detector

Run the application:

python app.py

Learning Outcomes

This project demonstrates practical understanding of:

Phishing detection
Email threat analysis
Python scripting
Security automation
URL inspection
Threat scoring
SOC-style investigation logic

Future Improvements

Planned improvements include:

Machine learning phishing classification
Streamlit web dashboard
Email file upload support
CSV logging
AI confidence score
Dataset-based model training
Disclaimer

This project is for educational and cybersecurity learning purposes only. It should only be used in authorized environments.

Author

Musa Chuene
GitHub: musechuene-commits