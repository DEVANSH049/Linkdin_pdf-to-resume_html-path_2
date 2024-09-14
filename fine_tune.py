from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
from feedback_handler import load_feedback

def fine_tune_model():
    """
    Fine-tunes google/flan-t5-base model using user feedback data.
    """
    # Load feedback data for retraining
    feedbacks = load_feedback()
    if not feedbacks:
        print("No feedback data available for retraining.")
        return

    # Load the pre-trained FLAN-T5 model and tokenizer
    model_name = "google/flan-t5-large"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    # Prepare training data
    inputs = [f"Original: {feedback['original']}\nEnhanced: " for feedback in feedbacks]
    targets = [feedback['enhanced'] for feedback in feedbacks]
    
    # Tokenize data
    input_encodings = tokenizer(inputs, padding=True, truncation=True, return_tensors="pt", max_length=512)
    target_encodings = tokenizer(targets, padding=True, truncation=True, return_tensors="pt", max_length=512)

    # Fine-tuning process
    optimizer = torch.optim.Adam(model.parameters(), lr=5e-5)
    model.train()  # Switch model to training mode
    
    for epoch in range(3):  # You can increase epochs depending on your dataset size
        optimizer.zero_grad()
        outputs = model(input_ids=input_encodings['input_ids'], labels=target_encodings['input_ids'])
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

    # Save the fine-tuned model
    model.save_pretrained('fine_tuned_flan_t5_model')
    tokenizer.save_pretrained('fine_tuned_flan_t5_model')
    print("Model fine-tuned and saved!")
