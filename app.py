
from scripts.query_RAG import query_rag
from flask import Flask, jsonify, request, render_template

#./mistral-7b-instruct-v0.2.Q4_0.llamafile

#./TinyLlama-1.1B-Chat-v1.0.F16.llamafile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('RetinaLLM.html')

@app.route('/results', methods=['POST'])
def results():
    query = request.form['query']
    response = query_rag(query)
    return render_template('RetinaLLM.html', query=query, response=response)

if __name__ == '__main__':
    app.run(debug=True)
