import streamlit as st
from langchain.schema.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader

#from langchain_community.document_loaders import PyPDFLoaderLoader
from langchain.chains.summarize import load_summarize_chain
from transformers import T5Tokenizer
from transformers import T5ForConditionalGeneration
from transformers import pipeline
import torch
import base64

#MODEL AND TOKENIZER
checkpoint = "LaMini-Flan-T5-248M"
tokenizer = T5Tokenizer.from_pretrained(checkpoint,legacy=False)
base_model = T5ForConditionalGeneration.from_pretrained(checkpoint, device_map = 'auto',torch_dtype = torch.float32)

#FILE LOADER AND PREPROCESSING
def file_preprocessing(file):
    loader = PyPDFLoader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=50)
    texts = text_splitter.split_documents(pages)
    fianl_texts = ""
    for text in texts:
        print(text)
        fianl_texts = fianl_texts + text.page_content
    return fianl_texts

#DEFINE LLM PIPELINE
def llm_pipeline(filepath):
    pipe_sum = pipeline(
        'summarization',
        model= base_model,
        tokenizer=tokenizer,
        max_length = 1000,
        min_length = 500,
    )
    input_text = file_preprocessing(filepath)
    result = pipe_sum(input_text)
    result = result[0]['summary_text']
    return result

@st.cache_data
def displayPDF(file):
    
    with open(file,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

#streamlit code
st.set_page_config(layout='wide',page_title="Summarization App")

def main():
    st.title("DOCUMENT SUMMARIZATION APP USING LANGUAGE MODEL")
    uploaded_file = st.file_uploader("UPLOAD YOUR PDF FILE📑",type=['pdf'])

    if uploaded_file is not None:
        if st.button("Summarize"):
            col1,col2 = st.columns(2)
            filepath = "data/"+uploaded_file.name
            with open(filepath,'wb') as temp_file:
                temp_file.write(uploaded_file.read())
            with col1:
                st.info("Uploaded PDF File")
                pdf_viewer=displayPDF(filepath)
            with col2:
                st.info("Summarization is below")

                summary = llm_pipeline(filepath)
                st.success(summary)

if __name__ == '__main__':
    main()
