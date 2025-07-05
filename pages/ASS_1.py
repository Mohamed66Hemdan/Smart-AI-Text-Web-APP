###########################################
# =========================================
# Library 
# =========================================
import streamlit as st
from streamlit_option_menu import option_menu
from transformers import pipeline
import pypdf

import base64
# =============================================
# Page Design
st.set_page_config(
    page_title="AI Models",
    page_icon="🤖",
    layout="wide",  
)
# 🔒 Hide Streamlit elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
# =========================================
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
        h1 , .stMarkdown p , label {{
        color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
image_path = r"images\img1.png"
set_bg_from_url(image_path)  
# # ============================================
# Const Variable
device = "cpu"
# # ============================================
###
# Warning Messsage
def custom_warning():
    st.markdown(f"""
        <div style="
            background-color: #fff3cd;
            color: #856404;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #ffeeba;
            font-weight: bold;
            font-size: 16px;
        ">
            ⚠️ Please enter some text to generate from.
        </div>
    """, unsafe_allow_html=True)
###
# =========================================
# Summarization Model
# Model 1 === Text Summarization Model 
# @st.cache_resource
def Summarization_Model(text):
    model_1 = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6", device=device)            
    result = model_1(user_input)
    st.markdown(f"""
    <div style="
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        font-weight: bold;
        font-size: 16px;
    ">
        ✅ {result[0]['summary_text']}
    </div>
    """, unsafe_allow_html=True)
    # st.success(result[0]['summary_text']) 
# =========================================
# =========================================
# Question Answering Model
# Model 2 === Question Answering Model 
def upload_pdf_fun():
    context_2 = ""
    uploaded_file = st.file_uploader("Upload PDF File", type="pdf")

    if uploaded_file is not None:
        reader = pypdf.PdfReader(uploaded_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                context_2 += page_text + "\n"

    return context_2
# =========================================
def Question_Answering(text = " ", context = ""):
    model_2 = pipeline("question-answering", model="deepset/bert-base-uncased-squad2")
    result_2 = model_2(question=text, context = context)
    st.markdown(f"""
    <div style="
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        font-weight: bold;
        font-size: 16px;
    ">
        ✅ {result_2['answer']}
    </div>
    """, unsafe_allow_html=True)
    # st.success(result_2['answer']) 
# =========================================
# =========================================
# Model 3 === Text Generation Model 
def Text_Generation_model_dialog(text):
    model_2_text_generation = pipeline("text-generation", model="microsoft/DialoGPT-small")
    result_model_2_text_generation = model_2_text_generation(text , max_length=100, pad_token_id=50256, do_sample=True,temperature=0.7, top_p=0.9,top_k=50)
    st.markdown(f"""
    <div style="
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        font-weight: bold;
        font-size: 16px;
    ">
        ✅ {result_model_2_text_generation[0]['generated_text']}
    </div>
    """, unsafe_allow_html=True)
    # st.success(result_model_2_text_generation[0]['generated_text']) 

def Text_Generation_model_BioGpt(text):
    model_2_text_generation = pipeline("text-generation", model="microsoft/biogpt")
    result_model_2_text_generation = model_2_text_generation(text,max_length=100,do_sample=False,num_return_sequences=1)
    st.markdown(f"""
    <div style="
        background-color: gray;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        font-weight: bold;
        font-size: 16px;
    ">
        ✅ {result_model_2_text_generation[0]['generated_text']}
    </div>
    """, unsafe_allow_html=True)
    # st.success(result_model_2_text_generation[0]['generated_text']) 

def Text_Generation_model_gpt2(text):
    model_2_text_generation = pipeline("text-generation", model="gpt2")
    result_model_2_text_generation = model_2_text_generation(text)
    st.markdown(f"""
    <div style="
        background-color: gray;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        font-weight: bold;
        font-size: 16px;
    ">
        ✅ {result_model_2_text_generation[0]['generated_text']}
    </div>
    """, unsafe_allow_html=True)
    # st.success(result_model_2_text_generation[0]['generated_text']) 
# =========================================
# =========================================
# =========================================
# Model 4 === Text Classification Model _ Text
def Text_Classification_From_Text(text):
    model_1 = pipeline("zero-shot-classification", model="Recognai/zeroshot_selectra_small") 
    labels = ['technology', 'science', 'politics', 'economy', 'sports']
    result = model_1(text, candidate_labels=labels)
    st.markdown(f"""
    <div style="
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        font-weight: bold;
        font-size: 16px;
    ">
        ✅ {result['labels'][0]}
    </div>
    """, unsafe_allow_html=True)

# =========================================
# Model 4 === Text Classification Model _ PDF
def Text_Classification(text):
    model_1 = pipeline("zero-shot-classification", model="Recognai/zeroshot_selectra_small") 
    labels = ['technology', 'science', 'politics', 'economy', 'sports']
    reader = pypdf.PdfReader(uploaded_file)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    
    sentences = [s.strip() for s in full_text.split('\n') if s.strip()]
    
    st.markdown("""
        <h2 style='color: white;'>🏷️ Classification Results</h2>
    """, unsafe_allow_html=True)    
    for sentence in sentences:
        result = model_1(sentence, candidate_labels=labels)
        top_label = result["labels"][0]
        st.markdown(f"**📝 Sentence:** {sentence}")
        
        st.markdown(f"""
        <div style="
            background-color: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #c3e6cb;
            font-weight: bold;
            font-size: 16px;
        ">
            ✅ {top_label}
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
# =========================================
###############################################################
###############################################################

# # 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu(
#         menu_title=None, 
#         options=["Text Summarization", "Question Answering", "Text Generation","Text Classification"],  
#     )
###############################################################
hide_sidebar = """
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)
###############################################################
st.markdown(
    """
    <style>
    div.block-container {
        margin-top: -100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
###############################################################
with st.container():
    selected = option_menu(
        menu_title="", 
        options=["Text Summarization", "Question Answering", "Text Generation", "Text Classification"],
        icons=["file-earmark-text", "question-circle", "robot", "tags"],
        menu_icon="list", 
        default_index=0,
        orientation="horizontal"
    )

st.write("---------------")
###############################################################
###############################################################
if selected == "Text Summarization":        
    st.title(f"📝 {selected} Model")
    st.markdown(""" Welcome to the Text Summarization app! This application uses the
                    [`sshleifer/distilbart-cnn-6-6`] Model
                    from Hugging Face Transformers to generate concise summaries of your text.""")  
    ###############################################################
    user_input = st.text_area("Enter Text" , height = 150, key="input_text")
    ###############################################################
    if st.button("🔍 Summarize Text"):
        if not user_input.strip():
            custom_warning()
        else:
            loading_msg = st.empty()
            loading_msg.markdown(
                "<h4 style='color: white;'>⏳ Summarizing... Please wait...</h4>",
                unsafe_allow_html=True
            )
            Summarization_Model(user_input)
            loading_msg.empty()
# =====================================================
###############################################################
###############################################################
if selected == "Question Answering":
    st.title(f"🧠 {selected} Model")
    st.markdown(""" This application leverages the powerful [`deepset/bert-base-uncased-squad2`] Model
                to provide accurate answers to your questions based on provided text.""")  
    ###############################################################
    user_input = st.text_area("Enter Text" , height = 150)
    context = upload_pdf_fun()
    ###############################################################
    
    if st.button("🔍 Answer Text"):
        if not user_input.strip():
            custom_warning()
        elif not context or context.strip() == "":
            custom_warning()
        else:
            loading_msg = st.empty()
            loading_msg.markdown(
                "<h4 style='color: white;'>⏳ Answering... Please wait...</h4>",
                unsafe_allow_html=True
            )
            Question_Answering(user_input, context)
            loading_msg.empty()
# =====================================================
###############################################################
###############################################################
if selected == "Text Classification":
    st.title(f"🗂️ {selected} Model")
    st.markdown(""" This application uses a machine learning model [`Recognai/zeroshot_selectra_small`] to automatically determine the topic of your text.
                Just enter a sentence or paragraph, and the model will classify it as one of the following categories:      
                - 🧠 **Politics**
                - ⚽ **Sports**
                - 🔬 **Science**
                - 💻 **Technology**
                - 💰 **Economy**""")  
    ###############################################################
    user_input = st.text_area("Enter Text" , height = 150, key="input_text")
    uploaded_file = st.file_uploader("Upload a PDF file with sentences", type=["pdf"])

    if st.button("🔍 Classify Text"):
        if uploaded_file is not None:
            loading_msg = st.empty()
            loading_msg.markdown(
                "<h4 style='color: white;'>⏳ Classification... Please wait...</h4>",
                unsafe_allow_html=True
            )
            Text_Classification(uploaded_file)
            loading_msg.empty()
        elif user_input.strip():
            loading_msg = st.empty()
            loading_msg.markdown(
                "<h4 style='color: white;'>⏳ Classification... Please wait...</h4>",
                unsafe_allow_html=True
            )
            Text_Classification_From_Text(user_input)
            loading_msg.empty()
        else:
            custom_warning()
# =====================================================

if selected == "Text Generation":
    # === Streamlit UI ===
    st.title("✍️ Text Generation Model")
    
    # Input text
    user_input = st.text_area("Enter your prompt:", height=150)
    
    # Model selector
    selected_model = st.selectbox("Choose a model:", ["Short Conversations / DialoGPT Model", "Medical Generation / BioGPT Model", "General Generation GPT-2"])
    
    # Button to trigger
    if st.button("🔍 Generate Text"):
        if not user_input.strip():
            # st.warning("Please enter some text to generate from.")
            custom_warning()
        else:
            if selected_model == "Short Conversations / DialoGPT Model":
                loading_msg = st.empty()
                loading_msg.markdown(
                    "<h4 style='color: white;'>⏳ Generation... Please wait...</h4>",
                    unsafe_allow_html=True
                )
                Text_Generation_model_dialog(user_input)
                loading_msg.empty()
            elif selected_model == "Medical Generation / BioGPT Model":
                # ✅ The symptoms of heart failure include 
                loading_msg = st.empty()
                loading_msg.markdown(
                    "<h4 style='color: white;'>⏳ Generation... Please wait...</h4>",
                    unsafe_allow_html=True
                )
                Text_Generation_model_BioGpt(user_input)
                loading_msg.empty()
            elif selected_model == "General Generation GPT-2":
                loading_msg = st.empty()
                loading_msg.markdown(
                    "<h4 style='color: white;'>⏳ Generation... Please wait...</h4>",
                    unsafe_allow_html=True
                )
                Text_Generation_model_gpt2(user_input)
                loading_msg.empty()
