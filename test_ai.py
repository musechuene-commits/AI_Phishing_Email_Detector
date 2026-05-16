from ai_detector import predict_email

email = input("Enter email text:\n\n")

result = predict_email(email)

print("\nAI Detection Result")
print("-" * 40)
print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']}%")