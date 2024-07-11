# Description: This script is used to create a chroma database for the RetinaLLM project.

# Importing required libraries
import os
import argparse
import shutil
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import LlamafileEmbeddings

# Defining the paths for the chroma database and location of the PDF files for RAG
chroma_path = "CHROMA_PATH"
data_path = "DATH_PATH"

# Loading the PDF documents


def docloader():
    """
    This function is used to load the PDF documents from the data path.

    Input:

    data_path: str

    Returns:

    docs: list[Document]
    """

    doc_loader = PyPDFDirectoryLoader(data_path)

    return doc_loader.load()


docs = docloader()


# splitting the documents into chunks


def chunking(docs: list[Document]):
    """

    This function is used to split the documents into chunks. After experimentation a chunk size of 1000 with an overlap of 200 was selected as the optimal configuration.


    Input:

    docs: list[Document]

    Returns:

    chunks: list[Document]

    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )

    return text_splitter.chunking(docs)


chunks = chunking(docs)

# creating the function to generate the embeddings


def get_embeddings():
    """
    This function is used to generate the embeddings for the documents. Llamafile embeddings are used. 

    Input:

    None

    Returns:

    embeddings

    """

    embeddings = LlamafileEmbeddings(base_url="http://host.docker.internal:8080")

    return embeddings


# generate chunk IDs so we can tell which document, page, and chunk the information is from


def chunk_ids(chunks):
    """

    This function generates chunk IDs so we can tell which document, page, and chunk the information is from.

    Input:

    chunks  (no chunk ID in metadata)

    Returns:

    chunks (chunk ID in metadata)

    """

    # initializing last page variable

    last_page = None

    # setting initial chunk index to 0
    chunk_index = 0

    # iterating through the chunks
    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page = f"{source}:{page}"

        # If we are on the same page, increase chunk index by 1
        if current_page == last_page:
            chunk_index += 1
        else:
            chunk_index = 0

        # Calculate the chunk ID by combining the page and chunk index
        chunk_id = f"{current_page}:{chunk_index}"

        # setting previous page equal to current page
        last_page = current_page

        # Add chunk ID to metadata
        chunk.metadata["id"] = chunk_id

    return chunks


# Adding chunks to the Chroma Database


def populate_chromadb(chunks: list[Document]):
    """
    This function is used to populate the Chroma database with the chunks. If the chunk already exists in the database it will be ignored.
    Only chunks with novel chunk IDs will be added to the database.

    Input:

    chunks: list[Document]

    Returns:

    None

    """

    # Load the existing database.
    db = Chroma(persist_directory=chroma_path, embedding_function=get_embeddings())

    # Calculate Page IDs.
    chunks_with_ids = chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)
