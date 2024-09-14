from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the FLAN-T5 model and tokenizer
model_name = "google/flan-t5-large"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def enhance_resume_fields(extracted_data):
    """
    Uses google/flan-t5-base to validate and enhance extracted resume data.
    """
    try:
        # Convert extracted data to a prompt for the FLAN-T5 model
        prompt = f"""
        Validate and enhance the following resume data:

        Name: {extracted_data.get('name', 'N/A')}
        Contact: {extracted_data.get('contact', 'N/A')}
        Experience: {extracted_data.get('experience', 'N/A')}
        Education: {extracted_data.get('education', 'N/A')}
        Skills: {extracted_data.get('top_skills', 'N/A')}
        
        Ensure everything is correct and properly formatted.
        """
        
        # Tokenize the prompt
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        
        # Generate the enhanced resume content using FLAN-T5
        outputs = model.generate(**inputs, max_length=512, num_beams=5, early_stopping=True)
        
        # Decode the model output into text
        enhanced_data = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return enhanced_data

    except Exception as e:
        return f"Error in LLM enhancement: {e}"
