from flask import Flask, request, redirect, url_for, render_template, jsonify
import json
from difflib import get_close_matches
from time import sleep

app = Flask(__name__)

# In-memory storage
storage = []
reviews = []

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

@app.route('/sql1')
def sql_1():
    return render_template('sql1.html')

@app.route('/sql2')
def sql_2():
    return render_template('sql2.html')

@app.route('/sql3')
def sql_3():
    return render_template('sql3.html')

@app.route('/javascript1')
def javascript_1():
    return render_template('javascript1.html')

@app.route('/sql2')
def javascript_2():
    return render_template('javascript2.html')

@app.route('/javasript3')
def javascript_3():
    return render_template('javascript3.html')

@app.route('/python1')
def python_1():
    return render_template('python1.html')

@app.route('/python2')
def python_2():
    return render_template('python2.html')
@app.route('/python3')
def python_3():
    return render_template('python3.html')

@app.route('/about')
def about():
    return render_template('about.html', reviews=reviews)

@app.route('/about/add', methods=['POST'])
def add_review():
    review = request.form['review']
    reviews.append(review)
    return redirect(url_for('about'))

@app.route('/reviews/delete/<int:review_id>')
def delete_review(review_id):
    if 0 <= review_id < len(reviews):
        reviews.pop(review_id)
    return redirect(url_for('about'))


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
        sleep(2)
        response = answer
    else:
        sleep(2)
        response = "I don't know the answer. Can you teach me?"
    
    return jsonify({'response': response})

@app.route('/update_knowledge', methods=['POST'])
def update_knowledge():
    user_input = request.json.get('user_input').lower()
    new_answer = request.json.get('new_answer')
    
    if new_answer:
        sleep(2)
        update_knowledge_base(user_input, new_answer, knowledge_base_file)
        response = "Thank you! I learned a new response! Please reload the script so I could fetch the new response from the knowledge base when requested."
    else:
        response = "Update skipped."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
