import streamlit as st

from send_email import send_email

st.header("Contact")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{message}
"""
    submit_btn = st.form_submit_button("Submit")
    if submit_btn:
        send_email(message)
        st.info("Your email was sent successfully")
