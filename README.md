# Heal Tech.AI Django API

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000)](https://github.com/yourusername/yourprojectname)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

Welcome to the Heal Tech.AI Django API repository! This API serves as the backend for the Heal Tech.AI web application, providing various AI-powered medical services. It includes endpoints for next word prediction, summarization, and question answering using pretrained language models.

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
