import re

PHISHING_KEYWORDS = [
    "urgent", "verify your account", "account suspended", "click here",
    "password expired", "login immediately", "unauthorized access",
    "confirm your identity", "bank account", "limited time",
    "security alert", "update your payment", "you have won",
    "claim your prize", "reset your password"
]

SUSPICIOUS_DOMAINS = [
    ".ru", ".cn", ".tk", ".xyz", ".top", ".click"
]


def detect_phishing(email_text):
    score = 0
    reasons = []

    text = email_text.lower()

    for keyword in PHISHING_KEYWORDS:
        if keyword in text:
            score += 15
            reasons.append(f"Suspicious keyword detected: '{keyword}'")

    urls = re.findall(r"https?://[^\s]+", email_text)

    for url in urls:
        score += 10
        reasons.append(f"URL detected: {url}")

        for domain in SUSPICIOUS_DOMAINS:
            if domain in url:
                score += 20
                reasons.append(f"Suspicious domain detected: {domain}")

    if "http://" in text:
        score += 10
        reasons.append("Insecure HTTP link detected")

    if len(re.findall(r"!", email_text)) >= 3:
        score += 10
        reasons.append("Excessive exclamation marks detected")

    if score >= 70:
        verdict = "HIGH RISK PHISHING"
    elif score >= 40:
        verdict = "SUSPICIOUS"
    else:
        verdict = "LOW RISK"

    return {
        "score": min(score, 100),
        "verdict": verdict,
        "reasons": reasons
    }