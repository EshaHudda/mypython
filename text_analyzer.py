def analyze_text_file(filepath):
    """Analyzes a text file and prints line, word, character counts, and the longest word."""

    try:
        with open(filepath, 'r') as file:
            content = file.read()

        lines = content.split('\n')
        line_count = len(lines)

        words = content.split()
        word_count = len(words)

        # Count characters excluding newlines
        char_count = len(content.replace('\n', ''))

        longest_word = ''
        for word in words:
            # Remove punctuation for accurate length comparison
            cleaned_word = ''.join(char for char in word if char.isalnum()) 
            if len(cleaned_word) > len(longest_word):
                longest_word = cleaned_word

        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters (excluding newlines): {char_count}")
        print(f"Longest word: {longest_word}")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")

# Example Usage
filepath = "your_text_file.txt"  # Replace with the actual file path
analyze_text_file(filepath)