from flask import Flask, render_template, request, jsonify
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from morse_lang.morse_map import MORSE_MAP
app = Flask(__name__)
REVERSE_MORSE_MAP = {v: k for k, v in MORSE_MAP.items()}

def morse_to_text(morse_code):
    """Convert morse code to text"""
    morse_chars = morse_code.split(' ')
    text = []
    
    for morse_char in morse_chars:
        if morse_char == '':
            if text and text[-1] != ' ':
                text.append(' ')
        elif morse_char in MORSE_MAP:
            text.append(MORSE_MAP[morse_char])
        else:
            text.append(f'[{morse_char}]') 
    
    return ''.join(text)

def text_to_morse(text):
    """Convert text to morse code"""
    morse = []
    
    for char in text.lower():
        if char == ' ':
            morse.append('') 
        elif char in REVERSE_MORSE_MAP:
            morse.append(REVERSE_MORSE_MAP[char])
        else:
            morse.append(f'[{char}]') 
    
    result = ' '.join(morse)
    result = result.replace('   ', '  ')
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/morse-to-text', methods=['POST'])
def morse_endpoint():
    data = request.json
    morse_code = data.get('morse', '')
    text = morse_to_text(morse_code)
    return jsonify({'text': text})

@app.route('/api/text-to-morse', methods=['POST'])
def text_endpoint():
    data = request.json
    text = data.get('text', '')
    morse = text_to_morse(text)
    return jsonify({'morse': morse})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
