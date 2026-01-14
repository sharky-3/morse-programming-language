#!/usr/bin/env python3
import sys
from .lexer import morse_to_text  # your Morse-to-text function

def main():
    if len(sys.argv) != 2:
        print("Usage: morse <file.mc>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".mc"):
        print("Error: file must end with .mc")
        sys.exit(1)

    # Read Morse code from file
    with open(filename, "r") as f:
        morse_code = f.read()

    # Translate Morse to Python code as text
    python_code = morse_to_text(morse_code)

    # Execute the translated Python code in a shared namespace
    namespace = {}  # this allows variables to persist in the execution
    try:
        exec(python_code, namespace)
    except Exception as e:
        print(f"Error executing code: {e}")

if __name__ == "__main__":
    main()
