# AI-Powered Phishing Email Detector

## Overview
This project is a Python-based phishing email detection tool designed to identify suspicious emails and potential phishing attempts using keyword analysis, URL inspection, and threat scoring techniques.

The tool scans email content for:
- Suspicious phishing keywords
- Unsafe URLs
- Suspicious domains
- Social engineering indicators
- Insecure HTTP links

It then calculates a threat score and provides a phishing verdict.

---

## Features

- Phishing keyword detection
- URL extraction and analysis
- Suspicious domain detection
- Threat scoring system
- SOC-style phishing alert output
- Lightweight and beginner-friendly

---

## Technologies Used

- Python
- Regular Expressions (re)

---

## Project Structure

```text
Syntecxhub_AI_Phishing_Email_Detector/
│
├── app.py
├── detector.py
├── README.md
├── requirements.txt
└── screenshots/
Installation

Clone the repository:

git clone https://github.com/musechuene-commits/AI_Phishing_Email_Detector.git

Move into the project directory:

cd AI_Phishing_Email_Detector

Run the application:

python app.py
Example Test Email
Urgent! Your bank account has been suspended. Click here to verify your account immediately: http://secure-bank-login.xyz
Example Output
Threat Score: 100%
Verdict: HIGH RISK PHISHING
Disclaimer

This project is intended for educational and cybersecurity learning purposes only.

Author

Musa Chuene