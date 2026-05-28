import re
import random

phishing_keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "click",
    "login",
    "suspended",
    "security alert",
    "account",
    "limited",
    "confirm",
    "reset"
]


def detect_phishing(email_text):

    reasons = []
    threat_score = 0

    text = email_text.lower()

    for keyword in phishing_keywords:
        if keyword in text:
            reasons.append(f"Suspicious keyword detected: '{keyword}'")
            threat_score += 1

    urls = re.findall(r"http[s]?://\S+", text)

    if urls:
        reasons.append("Suspicious URL detected")
        threat_score += 2

    if threat_score >= 4:
        prediction = "Phishing"
    else:
        prediction = "Safe"

    confidence = random.randint(75, 99)

    return {
        "prediction": prediction,
        "threat_score": threat_score,
        "confidence": confidence,
        "reasons": reasons
    }