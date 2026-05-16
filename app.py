from detector import detect_phishing

print("=" * 60)
print("AI-Powered Phishing Email Detector")
print("=" * 60)

email_text = input("\nPaste the email/message you want to scan:\n\n")

result = detect_phishing(email_text)

print("\n" + "=" * 60)
print("SCAN RESULT")
print("=" * 60)
print(f"Threat Score: {result['score']}%")
print(f"Verdict: {result['verdict']}")

print("\nReasons:")
if result["reasons"]:
    for reason in result["reasons"]:
        print(f"- {reason}")
else:
    print("- No strong phishing indicators detected.")