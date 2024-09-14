import streamlit as st
from extract_pdf import extract_pdf_sections
from llm_enhancer import enhance_resume_fields
from feedback_handler import save_feedback

# Streamlit app
st.title("Resume Analyzer")

# PDF Upload
uploaded_file = st.file_uploader("Upload a resume PDF", type="pdf")

if uploaded_file is not None:
    with st.spinner('Extracting data...'):
        # Extract resume data
        extracted_data = extract_pdf_sections(uploaded_file)
        st.success("Extraction complete!")
        st.write(extracted_data)

        # Enhance using LLM
        enhanced_data = enhance_resume_fields(extracted_data)
        st.write("Enhanced Resume Data:", enhanced_data)

        # Feedback mechanism
        if st.button("Submit Feedback"):
            feedback = st.text_area("Provide feedback for the extracted/enhanced data")
            if feedback:
                feedback_data = {"original": extracted_data, "enhanced": enhanced_data, "feedback": feedback}
                save_feedback(feedback_data)
                st.success("Thank you for your feedback!")
