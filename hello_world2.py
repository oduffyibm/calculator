import streamlit as st
from udfs import *

###########
dev_mode = True
###########

def clear_index():
    st.session_state["index"] = ""

####
if dev_mode:
    ibm_api_key = st.secrets["api_key"]
    deployment_url = st.secrets["umiami_deployment_url"]
else:
    with st.sidebar:
        ibm_api_key = st.text_input("IBM Cloud API Key", key="chatbot_api_key", type="password")
        deployment_url = st.text_input("Public Text endpoint", key="deployment_url", type="password")
####
              
st.title("UMiami Social Media Analysis with watsonx.ai")

uploaded_file_1 = st.file_uploader("Upload an article", type=("txt", "md", "pdf"), on_change=clear_index, key="1")
# uploaded_file_2 = st.file_uploader("Upload an article", type=("txt", "md", "pdf"), on_change=clear_index, key="2")

if uploaded_file_1 and ibm_api_key:

    pdf_1 = parse_pdf(uploaded_file_1)
    
    
    question = st.text_area(
        "Ask something about the tweets",
        value="Provide me a sentiment analysis summary of the tweets",

        disabled=not uploaded_file_1,)
    if question:
        print("Question = " + question)

        
        with st.spinner('Thinking...'):
            msg = make_scoring_request(ibm_api_key, deployment_url, {"document1": pdf_1, "question": question})['results'][0]['generated_text']
            
            st.write("### Answer")
                
            st.write(msg)