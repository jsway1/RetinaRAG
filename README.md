# AIPI 561 Project: Surgery LLM

For decades now, surgical trainees have relied on information from textbooks and "real-time" instruction from attending surgeons in the OR during residency. The authors of the The Duke Manuals of Ophthalmic Surgery aimed to to improve upon this by creating a textbook series that contains traditional surgical information, as well tips/tricks from attending surgeons for each type of procedure. The goal of this project was to create a local llamafile based RAG system with access to these textbooks. This will allow ophthalmology residents to interact with the information in real time and help them prepare for OR cases and their board exams. If trainees find this system useful, we will expand this effort to cover other medical specialties. 

# Data

The system was trained on PDFs provided by the authors of the Duke Manual of Vitreoretinal Surgery. Each PDF corresponds to a chapter of the textbook and describes case preparation, surgical technique, tips and tricks, and common complications for each case type. A total of 69 PDF documents from this textbook were used in RAG development. This information is protected by copyright, so we were not able to publish these PDFs along with this repository. We have included open source sample PDFs describing common conditions in vitreoretinal surgery to allow prospective users to test the system.

# Setup

Download your llamafile of choice from the Mozilla Ocho Repository: https://github.com/Mozilla-Ocho/llamafile

This system was developed with the Mistral-7B-Instruct model 

Once you have downloaded your llamafile of choice, follow the quickstart guidelines on the same webpage to get your local LLM up and running. 

# Instructions



# Comparison



