from collections import defaultdict

# Function to count the number of words in the text
def count_words(text):
    words = text.split()
    return len(words)

# Function to count the frequency of each character (only alphabetic)
def count_characters(text):
    char_count = defaultdict(int)

    # Convert text to lowercase to make the count case-insensitive
    text = text.lower()

    # Loop through each character in the text
    for char in text:
        # Only count alphabetic characters
        if char.isalpha():
            char_count[char] += 1

    # Convert defaultdict to a regular dict
    return dict(char_count)

# Function to generate a sorted report
def generate_report(word_count, char_count):
    # Sort the characters by their frequency in descending order
    sorted_char_count = sorted(
        [{"char": char, "num": count} for char, count in char_count.items()],
        key=lambda x: x["num"], reverse=True
    )

    # Print the report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    # Print character frequencies
    for entry in sorted_char_count:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    
    print(f"--- End report ---")

def main():
    # Specify the path to the file
    path_to_file = "books/frankenstein.txt"

    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    # Count words and characters
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    # Generate and print the report
    generate_report(word_count, char_count)

# Call the main function to execute the program
if __name__ == "__main__":
    main()