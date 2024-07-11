from scripts.query_RAG import query_rag
from flask import Flask, request, render_template
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("RetinaLLM.html")


@app.route("/results", methods=["POST"])
def results():
    query = request.form["query"]
    response = query_rag(query)
    return render_template("RetinaLLM.html", query=query, response=response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
