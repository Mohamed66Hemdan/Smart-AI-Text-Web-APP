###########################################
# =========================================
# Library 
# =========================================
import streamlit as st
import base64
# =========================================
# Page Information 
st.set_page_config(
    page_title="Home Page",
    page_icon="🏠",
    layout="wide",  
    initial_sidebar_state="collapsed", 
)
# =========================================
# 🔒 Hide Streamlit elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
# =========================================
# Image Url
def set_bg_from_url(image_url):
    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .main-button {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 10vh;
        }}
        .stButton > button{{
            font-size: 30px ;
            padding: 0.75em 2em;
            border-radius: 12px;
            background-color: #000;
            color: #FFF;
            border: none;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            cursor: pointer;
            transition: 0.3s;
            margin-left: 40%;

        }}
        .stButton > button:hover {{
            background-color: #f0f0f0;
            color: #111;
            
        }}
    
        </style>
        """,
        unsafe_allow_html=True
    )
image_path = r"C:\Users\Dell\Artificial Intelligence\Generative AI\Assignments\ASS_1\images\img1.png"
set_bg_from_url(image_path)  

# st.title("Smart Text AI")

st.markdown("<h1 style='text-align: center; color: white; font-size: 70px;'>Smart Text AI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white; font-size: 30px;'>Summarize, Generate, Classification and Question Answering — All in One</h3>", unsafe_allow_html=True)

st.markdown("<div class='main-button';  style='text-align: center;' >", unsafe_allow_html=True)
# زر الاستمرار
if st.button("Let's Go 🔥"):
    st.switch_page("pages\ASS_1.py")
st.markdown("</div>", unsafe_allow_html=True)
