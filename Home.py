import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Bence.jpg")

with col2:
    st.title("Bence Stáb")
    content = """
        Hello, I'm Bence Stáb, a junior Python developer with a strong passion for technology.
         I'm highly enthusiastic about coding and constantly exploring new ways to leverage Python to
          create innovative solutions. I'm eager to collaborate, learn, and grow in the exciting world
          of software development.
        """
    st.info(content)

content2 = """
            Below, you'll find a few projects I've worked on using Python. Feel free to reach out if you're
            interested in similar projects or if you have any questions.
            """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
