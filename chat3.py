from flask import Flask, request, redirect, url_for, render_template, jsonify
import json
from difflib import get_close_matches

app = Flask(__name__)

# In-memory storage
storage = []

def load_knowledge_base(file_path: str) -> dict:
    """Load the knowledge base from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, create a new knowledge base
        data = {"questions": []}
    return data

def save_knowledge_base(file_path: str, data: dict):
    """Save the knowledge base to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    """Find the best matching question from the knowledge base."""
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    """Get the answer for a specific question from the knowledge base."""
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def update_knowledge_base(user_question: str, new_answer: str, file_path: str):
    """Update the knowledge base with a new question-answer pair."""
    knowledge_base = load_knowledge_base(file_path)
    knowledge_base["questions"].append({"question": user_question, "answer": new_answer})
    save_knowledge_base(file_path, knowledge_base)

# Load the knowledge base file
knowledge_base_file = 'knowledge_base.json'
knowledge_base = load_knowledge_base(knowledge_base_file)

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html', storage=storage)

@app.route('/store', methods=['POST'])
def store():
    info = request.form.get('info')
    if info:
        storage.append(info)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['GET'])
def delete(index):
    if 0 <= index < len(storage):
        storage.pop(index)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html', response="")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input').lower()
    
    # Find the best match from the knowledge base
    best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    
    if best_match:
        answer = get_answer_for_question(best_match, knowledge_base)
        response = answer
    else:
        response = "I don't know the answer. Can you teach me?"
    
    return jsonify({'response': response})

@app.route('/update_knowledge', methods=['POST'])
def update_knowledge():
    user_input = request.json.get('user_input').lower()
    new_answer = request.json.get('new_answer')
    
    if new_answer:
        update_knowledge_base(user_input, new_answer, knowledge_base_file)
        response = "Thank you! I learned a new response!"
    else:
        response = "Update skipped."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
