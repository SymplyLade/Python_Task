# question 13
import re
# Personal domains
personal = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
pattern = r'^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}$'
# --- Terminal Version ---
email = input("Enter your email: ").strip().lower()
if re.match(pattern, email):
    user, domain = email.split("@")
    cat = "Personal Email" if domain in personal else "Corporate/Other Email"
    print(f"\n--- Email Details ---\nEmail: {email}\nUsername: {user}\nDomain: {domain}\nCategory: {cat}\nLength: {len(email)}")
else:
    print("Invalid email format.")
# --- Streamlit Version ---
try:
    import streamlit as st
    st.title(":e-mail: Email Slicer")
    e = st.text_input("Enter your email").strip().lower()
    if e:
        if re.match(pattern, e):
            u, d = e.split("@")
            c = "Personal Email" if d in personal else "Corporate/Other Email"
            st.write(f"**Email:** {e}\n**Username:** {u}\n**Domain:** {d}\n**Category:** {c}\n**Length:** {len(e)}")
        else:
            st.error("Invalid email format.")
except:
    pass