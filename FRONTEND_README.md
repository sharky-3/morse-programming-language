# Morse Code Translator Frontend

A beautiful web interface for translating between text and Morse code using your `morse_map.py`.

## Features

- ✨ **Clean, Modern UI** - Beautiful responsive design
- 🔄 **Bidirectional Translation** - Convert text to Morse and vice versa
- 📋 **Copy to Clipboard** - Easy sharing of translations
- 📚 **Morse Code Reference** - Quick lookup guide
- ⚡ **Real-time Processing** - Instant translations

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Open in Browser
Navigate to `http://localhost:5000` in your web browser.

## Usage

### Text to Morse
1. Enter text in the left panel
2. Click "Translate" button (or press Ctrl+Enter)
3. View and copy the Morse code

### Morse to Text
1. Enter Morse code in the right panel (dots, dashes, and spaces)
2. Click "Translate" button (or press Ctrl+Enter)
3. View and copy the translated text

## Morse Code Syntax
- Dots (.) and dashes (-) represent individual characters
- Single spaces separate different characters
- Double spaces separate words

Example: `.--. .... .. .-..` = "phil"

## File Structure
```
morse-programming-language/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Web interface
└── requirements.txt      # Python dependencies
```

## Customization

You can modify the `morse_map.py` or add more characters by editing the MORSE_MAP dictionary in `app.py`.

## Troubleshooting

**Port already in use**: Change the port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use 5001 instead
```

**Module not found**: Ensure you're in the correct directory and have run:
```bash
pip install -e .
```
