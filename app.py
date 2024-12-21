from flask import Flask, request, jsonify
import os
from PIL import Image
import pytesseract
import random

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_images():
    images = request.files.getlist('images')
    questions = []
    for image in images:
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        question, *options = text.split('\n')
        questions.append({
            'question': question.strip(),
            'options': [opt.strip() for opt in options if opt]
        })
    return jsonify({'questions': questions})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_index = data['questionIndex']
    option_index = data['optionIndex']
    # Placeholder logic. Replace with actual AI model.
    is_correct = random.choice([True, False])
    return jsonify({'message': 'Correct!' if is_correct else 'Incorrect'})

if __name__ == '__main__':
    app.run(debug=True)
