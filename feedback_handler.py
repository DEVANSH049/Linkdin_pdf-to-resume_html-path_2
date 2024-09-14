import json

FEEDBACK_FILE = 'feedback.json'

def save_feedback(feedback_data):
    """
    Saves feedback data into a JSON file.
    """
    try:
        with open(FEEDBACK_FILE, 'a') as f:
            f.write(json.dumps(feedback_data) + "\n")
        return "Feedback saved successfully."
    except Exception as e:
        return f"Error saving feedback: {e}"

def load_feedback():
    """
    Loads all feedback for training or analysis.
    """
    try:
        feedbacks = []
        with open(FEEDBACK_FILE, 'r') as f:
            for line in f:
                feedbacks.append(json.loads(line.strip()))
        return feedbacks
    except FileNotFoundError:
        return []
