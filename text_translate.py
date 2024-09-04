from deep_translator import GoogleTranslator

# Input and output file paths
input_file_path = 'input.txt'
output_file_path = 'translated.txt'
words_per_line = 15  # Number of words per line

# Ask the user for the desired target language
target_language = input("Enter the target language code (e.g., 'bg' for Bulgarian, 'es' for Spanish): ")

# Read the content of the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Translate the text
translator = GoogleTranslator(source='auto', target=target_language)
translated_text = translator.translate(text)

# Split the translated text into words
words = translated_text.split()

# Chunk words into lines with a maximum of `words_per_line` words
chunked_lines = [' '.join(words[i:i + words_per_line]) for i in range(0, len(words), words_per_line)]

# Write the chunked lines to the output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(chunked_lines))

print(f"Translated text successfully written to {output_file_path}.")
