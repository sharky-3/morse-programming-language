#!/usr/bin/env python3
import sys
from .lexer import morse_to_text

def main():
    """Main entry point for the morse command-line tool."""
    if len(sys.argv) != 2:
        print("Usage: morse <file.mc>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".mc"):
        print("Error: file must end with .mc")
        sys.exit(1)

    # Read Morse code from file
    try:
        with open(filename, "r") as f:
            morse_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Translate Morse to Python code as text
    python_code = morse_to_text(morse_code)

    # Execute the translated Python code in a shared namespace
    namespace = {}
    try:
        exec(python_code, namespace)
    except Exception as e:
        print(f"Error executing code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
