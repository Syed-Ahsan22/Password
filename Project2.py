import re
import streamlit as st

#page styling 
st.set_page_config(page_title="Password Strength Checker By Syed Developer", page_icon="🌘", layout="centered")

#Css
st.markdown(""" 
<style> 
            .main {text-align: center;}
            .stTextInput {width: 60% !important; margin: auto;}
            .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px:}
            .stButton button:hover { background-color: #45a049;}
            </style>
            """, unsafe_allow_html=True)

#page title

st.title("🔐 Password Strength Generator")
st.write(" Enter Your Password Below to Check its Security Level. 🔍")

#check password strenght

import re

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        print("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        print("✅ Strong Password!")
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")

# Get user input
password = input("Enter your password: ")
check_password_strength(password)

#Buttom working

if st.button("Check Strength"):
    if password:
          check_password_strength(password)
    else :
            st.warning("⚠️ Please Enter the Password!")
