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

email_text = st.text_area(
    "Paste suspicious email content below:",
    height=250
)

if st.button("Scan Email"):

    if email_text.strip() == "":
        st.warning("Please paste an email message first.")
    else:

        result = detect_phishing(email_text)

        if result["prediction"] == "Phishing":
            st.error("⚠️ Potential Phishing Email Detected")
        else:
            st.success("✅ Email Appears Safe")

        st.subheader("Detection Details")

        st.write(f"**Prediction:** {result['prediction']}")
        st.write(f"**Threat Score:** {result['threat_score']}")
        st.write(f"**AI Confidence:** {result['confidence']}%")

        st.subheader("Reasons")

        for reason in result["reasons"]:
            st.write(f"- {reason}")