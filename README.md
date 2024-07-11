# AIPI 561 Project: Vitreoretinal Surgery LLM

For decades now, surgical trainees have relied on information from textbooks and "real-time" instruction from attending surgeons in the OR during residency. The authors of the The Duke Manuals of Ophthalmic Surgery aimed to to improve upon this by creating a textbook series that contains traditional surgical information, as well tips/tricks from attending surgeons for each type of procedure. The goal of this project was to create a local llamafile based RAG system with access to the Duke Manual of Vireoretinal Surgery. This will allow ophthalmology residents and vitreoretinal surgery fellows to interact with the information in real time and help them prepare for OR cases and their board exams. If trainees find this system useful, we will expand this effort to cover other medical specialties/subspecialties. 

Developing the system architecture involved sourcing chapter PDFs from the publisher, creating text chunks, embedding text chunks, and storing them in a Chroma database. User queries are entered through a simple HTML/Flask interface and embeddings are generated for these queries. The top 3 most similar text passages to the user query are extracted from the Chroma database using semantic search. These text passages are fed into a local llamafile language model (Mistral 7B) along with the user query and a prompt. The prompt used was as follows: 

#### LLM Prompt: 

Answer the question based only on the following context:

You are an experienced vitreoretinal surgeon speaking with trainees. You can answer detailed questions about vitreoretinal surgery concisely and accurately. Keep response length short (within 100 words if possible).

The system generates a response which is fed back to the user through the HTML/Flask interface. A diagram of the system architecture is provided below: 

<img width="750" alt="Screenshot 2024-07-01 at 4 52 33 PM" src="https://github.com/jsway1/RetinaRAG/assets/45215554/45bb9cf5-f558-4d2f-a843-266d6f3b355e">

#### Performance Evaluation

The performance of the Mistral 7B Instruct model was evaluated both with and without RAG augmentation. Responses were compared to an ideal response (sourced from the text) via cosine similarity. Results are provided in the plot below. The RAG system outperformed the LLM-only approach for all questions, but to varying degrees. The LLM-only approach struggled to provide concise answers for more complex questions without RAG augmentation. The code for this comparison is provided in the "notebooks" folder. The questions used are provided in the "model_eval_questions.txt" text file. 


<img width="600" alt="Screenshot 2024-07-10 at 3 50 45 PM" src="https://github.com/jsway1/RetinaRAG/assets/45215554/4e3d79f4-1b45-4af2-93e9-2d77205a5a6d">


#### Link to Demo Video: 




# Instructions for Setup, Running, and Testing Application 

## Setup

Download the Mistral 7B Instruct llamafile from the Mozilla Ocho Repository: https://github.com/Mozilla-Ocho/llamafile


<img width="826" alt="Screenshot 2024-07-02 at 2 55 34 PM" src="https://github.com/jsway1/AIPI_561_LLM/assets/45215554/c7eb02b7-5054-41b2-927f-796d67b533e6">


Once you have downloaded the Mistral 7B llamafile run the following command in your command line to grant permission for your computer to run the model (only need to do this once) 

chmod +x mistral-7b-instruct-v0.2.Q4_0.llamafile

You can then activate the model by running: 

./mistral-7b-instruct-v0.2.Q4_0.llamafile

## Running the Application 

Once you have activated your llamafile, make sure your system has all required packages (in requirements.txt file). 

After confirming package installation run the following command in the terminal to activate the system. 

python3 app.py 

The system will prompt you to open a webpage at localhost:5000 where you should see the RetinaLLM frontend. You can now ask questions to the RAG application 

![image](https://github.com/jsway1/AIPI_561_LLM/assets/45215554/063f0775-3001-4965-ac73-43f8164f1fdf)












# Repository Folders and Contents 

## docs

The system was trained on PDFs provided by the authors of the Duke Manual of Vitreoretinal Surgery. This information is protected by copyright, so we were not able to publish these PDFs along with this repository. We have included open source sample PDFs describing common conditions in vitreoretinal surgery to allow prospective users to test the database creation system. 

## chroma 

Contains files associated with the chroma database that stores the text chunk embeddings from the textbook chapters used.

## notebooks 

Contains Jupyter notebooks used during the app development process 

## scripts 

createdb.py  - script that contains text chunk generation, text chunk embedding, and chroma database creation code 

query_RAG.py  - script that contains RAG query function 

## templates 

RetinaLLM.html - html template for Flask/HTML user interface





