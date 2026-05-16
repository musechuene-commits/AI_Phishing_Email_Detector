import pickle

with open("phishing_model.pkl", "rb") as file:
    model = pickle.load(file)


def predict_email(email_text):
    prediction = model.predict([email_text])[0]
    confidence = model.predict_proba([email_text]).max()

    return {
        "prediction": prediction,
        "confidence": round(confidence * 100, 2)
    }