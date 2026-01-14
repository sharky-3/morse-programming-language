#!/usr/bin/env python3
import sys
from .lexer import morse_to_text

def main():
    if len(sys.argv) != 2:
        print("Usage: morse <file.mc>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".mc"):
        print("Error: file must end with .mc")
        sys.exit(1)

    with open(filename, "r") as f:
        morse_code = f.read()

    # Translate Morse to text
    text_code = morse_to_text(morse_code)

    # Just print the translated text
    print(text_code)

if __name__ == "__main__":
    main()
