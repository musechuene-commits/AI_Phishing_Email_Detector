import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle

# Sample phishing dataset
data = {
    "email": [
        "Urgent! Verify your bank account now",
        "Click here to reset your password",
        "You won a free prize claim now",
        "Security alert login immediately",
        "Update your payment information now",
        "Confirm your identity immediately",
        "Your account has been suspended",
        "Limited time offer click here now",

        "Meeting scheduled for tomorrow",
        "Please review the attached report",
        "Lunch meeting at 1PM",
        "Your support ticket has been updated",
        "Monthly system maintenance notification",
        "Project meeting rescheduled to Friday",
        "Please find attached the invoice",
        "Team meeting starts at 10AM"
    ],

    "label": [
        "phishing",
        "phishing",
        "phishing",
        "phishing",
        "phishing",
        "phishing",
        "phishing",
        "phishing",

        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe",
        "safe"
    ]
}

# Create dataframe
df = pd.DataFrame(data)

# Features and labels
X = df["email"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Build ML pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print("AI PHISHING DETECTION MODEL")
print("=" * 50)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
with open("phishing_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully.")