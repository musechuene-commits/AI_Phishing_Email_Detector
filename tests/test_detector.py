def test_basic_phishing_keywords():
    phishing_text = "Urgent! Your account will be suspended. Click here to verify your password."
    assert "urgent" in phishing_text.lower()
    assert "password" in phishing_text.lower()