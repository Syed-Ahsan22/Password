import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Syed Developer", page_icon="🌘", layout="centered")

# Custom CSS
st.markdown(""" 
<style> 
    .main {text-align: center;}
    .stTextInput > div > div > input {
        width: 60% !important;
        margin: auto;
    }
    .stButton > button {
        width: 50%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# Page title and subtitle
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

# Password strength checker function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# User input
password = st.text_input("🔑 Enter Password", type="password")

# Check button
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
        
        for item in feedback:
            st.info(item)
    else:
        st.warning("⚠️ Please enter a password!")
