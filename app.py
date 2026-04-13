import streamlit as st
import streamlit.components.v1 as components
import os



st.set_page_config(layout="wide")
st.title("Agreement Analysis Dashboard")

html_dir = "res/HTML"

# get all html files
files = sorted([f for f in os.listdir(html_dir) if f.endswith(".html")])

for file in files:
    st.subheader(file.replace(".html", "").replace("_", " ").title())
    
    path = os.path.join(html_dir, file)
    
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()
        components.html(html_content, height=600, scrolling=True)