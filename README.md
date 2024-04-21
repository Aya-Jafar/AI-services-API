# Heal Tech.AI Django API

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000)](https://github.com/yourusername/yourprojectname)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

Welcome to the Heal Tech.AI Django API repository! This API serves as the backend for the Heal Tech.AI web application, providing various AI-powered medical services. It includes endpoints for next word prediction, summarization, and question answering using pretrained language models.

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/yourusername/yourprojectname.git

2. Navigate to the project directory:
   ```sh
   cd collegeDjango

3. python -m venv venv
4. Activate python environment
   
  Window:
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
      "long_text": "Example Long text"
  }

- **Response**
  ```json
  {
       "summarized_text": "Appendicitis"
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


  






  
