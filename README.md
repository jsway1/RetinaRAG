# AIPI 561 Project: Surgery LLM

For decades now, surgical trainees have relied on information from textbooks and "real-time" instruction from attending surgeons in the OR during residency. The authors of the The Duke Manuals of Ophthalmic Surgery aimed to to improve upon this by creating a textbook series that contains traditional surgical information, as well tips/tricks from attending surgeons for each type of procedure. The goal of this project was to create a local llamafile based RAG system with access to the Duke Manual of Vireoretinal Surgery. This will allow ophthalmology residents and vitreoretinal surgery fellows to interact with the information in real time and help them prepare for OR cases and their board exams. If trainees find this system useful, we will expand this effort to cover other medical specialties/subspecialties. 

Developing the system architecture involved sourcing chapter PDFs from the publisher, creating text chunks, embedding text chunks, and storing them in a Chroma database. User queries are entered through a simple HTML/Flask interface and embeddings are generated for these queries. The top 3 most similar text passages to the user query are extracted from the Chroma database using semantic search. These text passages are fed into a Mistral 7B language model along with the user query and a prompt. The prompt used was as follows: 

LLM Prompt: 

Answer the question based only on the following context:

You are an experienced vitreoretinal surgeon speaking with trainees. You can answer detailed questions about vitreoretinal surgery concisely and accurately. Keep response length short (within 100 words if possible).

The system generates a response which is fed back to the user through the HTML/Flask interface. A diagram of the system architecture is provided below: 

![image](https://github.com/jsway1/AIPI_561_LLM/assets/45215554/8b9c9a8e-d466-4158-8d68-fd1f19fc7972)



# Performance Evaluation







# Setup

Download your llamafile of choice from the Mozilla Ocho Repository: https://github.com/Mozilla-Ocho/llamafile

This system was developed with the Mistral-7B-Instruct model 

Once you have downloaded your llamafile of choice, follow the quickstart guidelines on the same webpage to get your local LLM up and running. 

# Instructions



# Comparison







A description of respository folders and contents is provided below. 

# Data

The system was trained on PDFs provided by the authors of the Duke Manual of Vitreoretinal Surgery. Each PDF corresponds to a chapter of the textbook and describes case preparation, surgical technique, tips and tricks, and common complications for each case type. A total of 69 PDF documents from this textbook were used in RAG development. This information is protected by copyright, so we were not able to publish these PDFs along with this repository. We have included open source sample PDFs describing common conditions in vitreoretinal surgery to allow prospective users to test the system.


