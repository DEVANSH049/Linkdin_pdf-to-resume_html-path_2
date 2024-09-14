#Linkdin_pdf-to-resume_html-path_2
This is a resume generator application built with Streamlit. The app allows users to upload a PDF resume, process it using a large language model (LLM), enhance and validate the extracted data, and generate a formatted HTML resume. Users can also provide feedback on the generated content, which is stored for future model improvements.

Model
This project uses the google/flan-t5-base model to process and enhance resume data extracted from PDF files. The model can be further fine-tuned using the fine_tune.py script to improve accuracy based on feedback.

Features
PDF Resume Upload: Users can upload a PDF resume via the Streamlit app.
LLM-Powered Extraction: Extracted text is processed and enhanced using the google/flan-t5-base model.
Feedback Mechanism: Users can provide feedback on the generated resume content, which is saved for future fine-tuning.
Customizable Resume Templates: Predefined templates for generating HTML resumes are available in the utils/resume_templates.py file.
