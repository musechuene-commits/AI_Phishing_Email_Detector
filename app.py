import streamlit as st
from detector import detect_phishing

st.set_page_config(
    page_title="AI Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI-Powered Phishing Email Detector")

st.markdown("""
Analyze suspicious emails and detect potential phishing attacks using
rule-based analysis and machine learning.
""")

st.divider()

email_text = st.text_area(
    "Paste suspicious email content below:",
    height=250
)

uploaded_file = st.file_uploader(
    "Or upload an email text file",
    type=["txt"]
)

if uploaded_file is not None:
    email_text = uploaded_file.read().decode("utf-8")
    st.text_area(
        "Uploaded Email Content",
        email_text,
        height=250
    )

if st.button("Scan Email"):
    if email_text.strip() == "":
        st.warning("Please paste or upload an email message first.")
    else:
        result = detect_phishing(email_text)

        st.divider()

        if result["prediction"] == "Phishing":
            st.error("⚠️ Potential Phishing Email Detected")
        else:
            st.success("✅ Email Appears Safe")

        st.subheader("Detection Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric("Prediction", result["prediction"])
        col2.metric("Threat Score", result["threat_score"])
        col3.metric("AI Confidence", f"{result['confidence']}%")

        st.subheader("Threat Score Level")
        st.progress(min(result["threat_score"] / 10, 1.0))

        st.subheader("Detection Reasons")

        if result["reasons"]:
            for reason in result["reasons"]:
                st.write(f"- {reason}")
        else:
            st.write("- No major phishing indicators detected.")

st.divider()

st.caption(
    "Educational cybersecurity project demonstrating phishing detection, "
    "Streamlit deployment, CI/CD, Docker, and DevSecOps practices."
)