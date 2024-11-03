# Question answering bot
The goal of this project is to develop a backend API that acts as a Question-Answering bot. This bot will leverage the capabilities of a large language model to answer questions based on the content of a document. The project involves using the Langchain framework to implement the Question-Answering functionality.

## Tech-stack
1) Flask as web-application
2) Ocrmypdf + fitz to extract PDF text
2) Pinecone DB to store vectors
3) OpenAI as LLM
4) Langchain to curate results using output from pinecone and LLM

## Endpoints
`POST /answer-question`

### Input/Payload
```
document_file: pdf file
questions_file: json file
```

### Output/Response
```
{ question1: answer1, question2: answer2, question3: answer3 }
```

## Instructions to run:
- Install Python3.10 
- Install dependencies from requirements.txt file using this command: `pip install -r requirements.txt`
- Install tesseract
  - For windows, from here: https://github.com/UB-Mannheim/tesseract/wiki, and add it to path
- Install Ghostscript
  - For windows, from here: https://ghostscript.com/releases/gsdnld.html, and add it to path

## Demo video
https://github.com/user-attachments/assets/1115e2d8-c943-4ba3-9fbd-d81df0e4d3ec

