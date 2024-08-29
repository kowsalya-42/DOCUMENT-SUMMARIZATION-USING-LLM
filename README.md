Welcome to the Document Summarization App! This Streamlit application allows you to easily upload PDF files and get concise summaries using advanced language models. Perfect for quickly extracting the essence of lengthy documents.

## ✨ Features
**PDF Upload:** Seamlessly upload your PDF documents.
**Text Summarization:** Get a summarized version of your document using state-of-the-art language models.
**Live PDF Display:** View your uploaded PDFs directly in the app.
**User-Friendly Interface:** Designed with a clean and intuitive UI for a smooth experience.
## 🛠️ Technology Stack
**Streamlit:** For building interactive web applications.
**LangChain:** For processing and summarizing text from documents.
**Transformers:** For using T5 model to generate summaries.
**PyTorch:** For deep learning computations.
**Base64:** For encoding PDF files for display.
## 📋 Requirements
To get started with this app, ensure you have the following Python packages installed:
***pip install streamlit langchain transformers torch***
## 🚀 How to Run
```
**Clone the Repository**
git clone https://github.com/yourusername/document-summarization-app.git
cd document-summarization-app
**Install Dependencies**
pip install -r requirements.txt
**Run the Application**
streamlit run app.py
Some basic Git commands are:
```

Upload a PDF and click the "Summarize" button to get your document summary.

## 📝 Code Explanation
**file_preprocessing(file):** Loads and preprocesses the PDF document, splitting it into manageable chunks.
**llm_pipeline(filepath):** Uses the T5 model to generate a summary of the preprocessed text.
**displayPDF(file):** Displays the uploaded PDF within the app using base64 encoding.
**main():** The main function that sets up the Streamlit interface and handles user interactions.

##📸 Screenshots
**🚀 Sleek Front End**
![Screenshot 2024-08-27 204053](https://github.com/user-attachments/assets/0ac76a51-a0de-4f99-ab28-bcd63c8c5abd)
**📄 Upload Your PDF Like a Pro**
![Screenshot 2024-08-27 204125](https://github.com/user-attachments/assets/75a90f13-c24d-4e13-a511-7bc4ee56a9bf)
**✨ Your Document Summarized in a Snap**
![Screenshot 2024-08-27 204310](https://github.com/user-attachments/assets/4a1d2375-c483-4b3c-be35-c2ee42a8a62b)

🔗 Links
Documentation: https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M
