from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load a pre-trained model for question answering
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

@app.route("/")
def home():
    # Serve the index.html file (ensure "templates/index.html" exists)
    return render_template('index.html')

# Example FAQ context
faq_context = """
Kongu Engineering College's Department of ECE focuses on research and education in AI, IoT, and embedded systems. 
Dr. S. Kumar is the HOD, with expertise in VLSI design.
The department organizes workshops, hackathons, and industry collaborations.
"""

@app.route("/chat", methods=["POST"])
def chatbot():
    user_input = request.json.get("question", "")
    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    # Generate response
    try:
        answer = qa_pipeline({"question": user_input, "context": faq_context})
        return jsonify({"answer": answer["answer"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
