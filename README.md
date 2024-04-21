# Heal Tech.AI Django API

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000)](https://github.com/yourusername/yourprojectname)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

Welcome to the Heal Tech.AI Django API repository! This API serves as the backend for the Heal Tech.AI web application, providing various AI-powered medical services. It includes endpoints for next word prediction, summarization, and question answering using pretrained language models.

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/Aya-Jafar/AI-services-API.git

2. Navigate to the project directory:
   ```sh
   cd collegeDjango

3. ```sh
   python -m venv venv
5. Activate python environment
   
  Windows:
  ```sh
    source venv/Scripts/activate
  ```
  MacOs:
  ```
  source venv/bin/activate
  ```
5. Install dependencies
   ```sh
   pip install -r requirements.txt
   
6. Run Server
   ```sh
   python manage.py runserver


## Endpoints

### Next Word Prediction

This endpoint takes a prompt as input and generates the next word prediction based on the provided prompt using a pretrained language model.

- **Endpoint:** `/generate/next-word/`
- **HTTP Method:** POST
- **Example Usage:**
  ```json
  {
      "prompt": "Once upon a time"
  }

- **Response**
  ```json
  {
      "generated_text": "there"
  }


### Summarization 

Takes a long text to summarize

- **Endpoint:** `/generate/summarize/`
- **HTTP Method:** POST
- **Example Usage:**
  ```json
  {
      "long_text": "Doctor: Good morning! How can I help you today?\nPatient: Hi, doctor. I've been experiencing some chest pain and shortness of breath lately.\nDoctor: I see. When did these symptoms start?\nPatient: It's been about a week now. The chest pain comes and goes, and I feel like I can't take a deep breath sometimes.\nDoctor: Have you noticed any other symptoms, such as coughing or fever?\nPatient: No coughing, but I've been feeling a bit tired and lightheaded.\nDoctor: Alright. Let's do a quick examination. I'll listen to your heart and lungs and take your blood pressure.\nPatient: Sure, doctor.\n[Doctor performs examination]\nDoctor: Your blood pressure is slightly elevated, and I hear some wheezing in your lungs. I'd like to run some tests to rule out any serious conditions. We'll start with an ECG and a chest X-ray.\nPatient: Okay, doctor. Should I be worried?\nDoctor: It's important to investigate further to determine the cause of your symptoms. Let's take one step at a time. I'll also prescribe you some medication to help with the chest pain and shortness of breath in the meantime.\nPatient: Thank you, doctor. I appreciate your help.\nDoctor: You're welcome. Let's get those tests done, and we'll go from there. I'll see you again soon for a follow-up.\n"
  }

- **Response**
  ```json
  {
       "summarized_text": "Doctor: Good morning! How can I help you today? Patient: Hi, doctor. I've been experiencing some chest pain and shortness of breath lately. Doctor: I see. When did these symptoms start? Patient: It's been about a week now. The chest pain comes and goes, and I feel like I can't take a deep breath sometimes. Doctor: Have you noticed any other symptoms, such as coughing or fever? Patient: No coughing, but I've been feeling a bit tired and lightheaded. Doctor: Alright. Let's do a quick examination. I'll listen to your heart and lungs and take your blood pressure. Patient: Sure, doctor. [Doctor performs examination] Doctor: Your blood"
  }



### QA model  

Takes a medical question and returns an answer

- **Endpoint:** `/generate/QA/`
- **HTTP Method:** POST
- **Example Usage:**
  ```json
  {
      "prompt": "What are the symptoms of appendicitis?"
  }

- **Response**
  ```json
  {
       "generated_text": "the symptoms of appendicitis can vary depending on the location of the infection, but common symptoms include abdominal pain, nausea, vomiting, and fever."
  }
