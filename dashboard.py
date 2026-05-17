import streamlit as st
from detector import detect_phishing
from ai_detector import predict_email

st.set_page_config(
    page_title="AI Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI-Powered Phishing Email Detector")

st.write(
    "Analyze emails using rule-based phishing detection "
    "and machine learning classification."
)

# Manual Email Input
email_text = st.text_area(
    "Paste email or message below:",
    height=220,
    placeholder="Example: Urgent! Verify your bank account immediately..."
)

# File Upload
uploaded_file = st.file_uploader(
    "Or upload a .txt email file",
    type=["txt"]
)

# Read uploaded file
if uploaded_file is not None:
    email_text = uploaded_file.read().decode("utf-8")

    st.subheader("Uploaded Email Content")
    st.code(email_text)

# Scan Button
if st.button("Scan Email"):

    if email_text.strip() == "":
        st.warning("Please paste email content or upload a file.")

    else:

        # Rule-Based Detection
        rule_result = detect_phishing(email_text)

        # AI Detection
        ai_result = predict_email(email_text)

        st.divider()

        # Rule-Based Results
        st.header("🔍 Rule-Based Detection")

        st.metric(
            "Threat Score",
            f"{rule_result['score']}%"
        )

        if rule_result["verdict"] == "HIGH RISK PHISHING":
            st.error(f"Verdict: {rule_result['verdict']}")

        elif rule_result["verdict"] == "SUSPICIOUS":
            st.warning(f"Verdict: {rule_result['verdict']}")

        else:
            st.success(f"Verdict: {rule_result['verdict']}")

        st.subheader("Detection Reasons")

        if rule_result["reasons"]:
            for reason in rule_result["reasons"]:
                st.write(f"- {reason}")
        else:
            st.write("- No strong phishing indicators detected.")

        st.divider()

        # AI Results
        st.header("🤖 AI / Machine Learning Detection")

        prediction = ai_result["prediction"]
        confidence = ai_result["confidence"]

        if prediction == "phishing":
            st.error(f"AI Prediction: {prediction.upper()}")
        else:
            st.success(f"AI Prediction: {prediction.upper()}")

        st.metric(
            "AI Confidence",
            f"{confidence}%"
        )

st.divider()

st.caption("Educational Cybersecurity Project by Musa Chuene")