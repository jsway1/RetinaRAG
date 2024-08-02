Vitreoretinal Surgery LLM

[![Docker Image CI](https://github.com/jsway1/RetinaRAG/actions/workflows/docker-image.yml/badge.svg)](https://github.com/jsway1/RetinaRAG/actions/workflows/docker-image.yml)

Surgical trainees traditionally rely on information from textbooks and real-time instruction from attending surgeons in the operating room. The authors of the The Duke Manuals of Ophthalmic Surgery aimed to to improve upon this model by creating a textbook series that contains both traditional surgical information as well tips/tricks from attending surgeons for each procedure. The goal of this project was to create a local llamafile-based RAG system with access to the Duke Manual of Vireoretinal Surgery. This will allow ophthalmology residents and vitreoretinal surgery fellows to interact with the information in real time and help them prepare for OR cases and their board exams. If trainees find this system useful, we will expand this effort to cover other medical specialties. 

Developing the system architecture involved sourcing chapter PDFs from the publisher, creating text chunks, embedding text chunks, and storing them in a Chroma database. User queries are entered through a simple HTML/Flask interface and embeddings are generated for these queries. The top 3 most similar text passages to the user query are extracted from the Chroma database using semantic search. These text passages are fed into a local llamafile language model (Mistral 7B Instruct) along with the user query and a prompt. The prompt used was as follows: 

#### LLM Prompt: 

_Answer the question based only on the following context:_

_You are an experienced vitreoretinal surgeon speaking with trainees. You can answer detailed questions about vitreoretinal surgery concisely and accurately. Keep response length short (within 100 words if possible)._

The system generates a response which is fed back to the user through the HTML/Flask interface. A diagram of the system architecture is provided below: 

<p align="center">
<img width="750" alt="Screenshot 2024-07-01 at 4 52 33 PM" src="https://github.com/jsway1/RetinaRAG/assets/45215554/45bb9cf5-f558-4d2f-a843-266d6f3b355e">
</p>

#### Performance Evaluation

The performance of the Mistral 7B Instruct model was evaluated both with and without RAG augmentation. Responses were compared to an ideal response (sourced from the text) via cosine similarity. Results are provided in the plot below. The RAG system outperformed the LLM-only approach for all questions, but to varying degrees. The LLM-only approach struggled to provide concise answers for more complex questions without RAG augmentation. The code for this comparison is provided in the "notebooks" folder. The average latency for all prompts was approximately 35 seconds with a range of 22 - 55 seconds and standard deviation of 10 seconds. The questions used are provided in the "model_eval_questions.txt" text file. 

<p align="center">
<img width="600" alt="Screenshot 2024-07-10 at 3 50 45 PM" src="https://github.com/jsway1/RetinaRAG/assets/45215554/4e3d79f4-1b45-4af2-93e9-2d77205a5a6d">
</p>

The Mistral 7B Instruct model was also compared to the TinyLlama-1.1B	model. The TinyLlama model had difficulty producing output on occasion and would return responses asking the user to find other sources for the requested information. As such, the Mistral 7B Instruct model was selected for further development tasks. 

#### Link to Demo Video: https://warpwire.duke.edu/w/O2QIAA/

# Instructions for Setup, Running, and Testing Application 

## Setup

Download the Mistral 7B Instruct llamafile from the Mozilla Ocho Repository: https://github.com/Mozilla-Ocho/llamafile

<p align="center">
<img width="826" alt="Screenshot 2024-07-02 at 2 55 34 PM" src="https://github.com/jsway1/AIPI_561_LLM/assets/45215554/c7eb02b7-5054-41b2-927f-796d67b533e6">
</p>

Once you have downloaded the Mistral 7B llamafile run the following command in your terminal to grant permission for your computer to run the model (only need to do this once) 

```
chmod +x mistral-7b-instruct-v0.2.Q4_0.llamafile
```

You must also clone this repository to your local machine. Navigate to the path you'd like to store the files then run the following command: 
   
```
git clone https://github.com/jsway1/RetinaRAG.git
```

## Running the Application 

Activate the model by running the following command (must be done every time you start the application): 

```
./mistral-7b-instruct-v0.2.Q4_0.llamafile
```

Create a virtual environment by running: 

```
python3 -m venv venv
```

Activate the virtual environment by running: 

```
source venv/bin/activate
```

Build the docker image by running: 

```
docker build -t retinarag -f Dockerfile.dockerfile .
```
After the docker image is created, run the following:  

```
docker run -p 5050:5050 retinarag
```  

The system will prompt you to open a webpage at localhost:5050 where you should see the RetinaLLM frontend. You can now ask questions to the RAG application 

<p align="center">
<img width="750" src="https://github.com/jsway1/AIPI_561_LLM/assets/45215554/063f0775-3001-4965-ac73-43f8164f1fdf">
</p>

## Testing the Application 

Create a virtual environment by running: 

```
python3 -m venv venv
```

Activate the virtual environment by running 

```
source venv/bin/activate
```

Install dependencies by running 

```
pip3 install -r requirements.txt
```

Test database access, embedding generation, LLM querying, and accuracy of responses by running the following command: 

```
pytest
```

You should receive a green message indicating that 4/4 tests passed 

# Repository Folders and Contents 

## app.py 

Main file that runs all components of the application 

## Dockerfile.dockerfile 

Dockerfile that creates docker image of application and runs app.py 

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

RetinaLLM.html - HTML template for Flask frontend 

## tests

test_RAG_application.py - script that tests app database access, embedding creation, LLM query, and response accuracy 

## model_eval_questions.txt

Contains 10 test questions and ideal answers used to evaluate performance of Mistral 7B Instruct model both with and without RAG 





