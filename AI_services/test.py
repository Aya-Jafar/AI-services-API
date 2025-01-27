import requests

next_word_url = "http://localhost:8000/generate/next-word/"
summarization_url = "http://localhost:8000/generate/summarize/"
qa_url = "http://localhost:8000/generate/QA/"

def predict_next_word(url, prompt):
    payload = {"prompt": prompt}
    response = requests.post(url, json=payload)
    return response.json()

def summarize_text(url, long_text):
    payload = {"long_text": long_text}
    response = requests.post(url, json=payload)
    return response.json()

def send_question(url, prompt):
    payload = {"prompt": prompt}
    response = requests.post(url, json=payload)
    return response.json()

# Next Word Prediction
next_word_response = predict_next_word(next_word_url, "Once upon a time")
print("Next Word Prediction Response:", next_word_response)

# Summarization
# summarization_response = summarize_text(summarization_url, "This is a long text that needs summarization.")
# print("Summarization Response:", summarization_response)

# # Question and Answer
# qa_response = send_question(qa_url, "Who is the president of the United States?")
# print("Question and Answer Response:", qa_response)
