import string
import random

# TODO Write docstrings for all functions
# TODO Write unit tests for all functions

def open_file(filename: str=""):
    if filename == "":
        filename = "book.txt"
    with open(filename) as file:
        text = file.read()
    return text

# TODO Compare with below implementation and choose best one

# def open_file(filename):
#     """Open the file with the given filename and return its contents as a string."""

#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             text = file.read()
#             return text
#     except FileNotFoundError:
#         print(f"Sorry, the file \"{filename}\" could not be found.")
#         return ""

def clean_text(text: str):
    """
    Cleans text by removing capitalisation and punctuation marks.
    Requires importing the built-in module "string".
    """

    #TODO Modify code to preserve punctuation inside words (e.g., the apostrophe in "don't")

    text = text.lower()
    for punctuation_mark in string.punctuation:
        text = text.replace(punctuation_mark, "") # TODO Check which is better replacement, nothing "" or space " "
    return text

def remove_duplicate_words(words: list):
    """Remove duplicate words from list of words."""

    # Use dict.fromkeys() method to create a dictionary with the words in the input list as keys, and None as the value for each key. This removes all duplicates from the original list, since a dictionary can only contain unique keys. The dictionary keys are then converted back into a list using the list() method.
    unique_words = list(dict.fromkeys(words))
    return unique_words

def print_words(words: list):
    """Print a list of words in alphabetical order with each word separated by a comma."""
    print(", ".join(sorted(words)))

def find_first_word(words: list):
    """Find the first word in the given text."""
    first_word = words[0]
    return first_word

def find_last_word(words: list):
    """Find the last word in the given text."""
    last_word = words[-1]
    return last_word

def find_first_character(text: str):
    """Find the first character in the given text."""
    first_character = text[0]
    return first_character

def find_last_character(text: str):
    """Find the last character in the given text."""
    last_character = text[-1]
    return last_character

def count_total_words(words: list):
    """Count the total number of words in the given text."""
    total_words = len(words)
    return total_words

def count_total_characters(text: str):
    """Count the total number of characters in the given text."""
    total_characters = len(text)
    return total_characters

def find_words_of_length(word_length: int, words: list):
    result = [word for word in words if len(word) == word_length]
    return result

def find_words_starting_with(letter: str, words: list):
    result = [word for word in words if word[0] == letter]
    # The above list comprehension is shorthand for the following

    # result = []
    # for word in words:
    #     if word[0] == letter:
    #         result.append(word)
    return result

def find_words_ending_with(letter: str, words: list):
    result = [word for word in words if word[-1] == letter]
    return result

def choose_random_word(words: list):
    """Choose a random word from the given text."""
    for _ in range(len(words)):
        random_index = random.randint(0, len(words) - 1)
        random_word = words[random_index]
        return random_word

def find_palindromes(words: list):
    """Find all palindromes consisting of 2 or more characters in the given text."""
    palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
    return palindromes

def find_shortest_unique_words(words: list):
    unique_words = {}

    for word in words:
        # Check if the word is already in the dictionary
        if word in unique_words:
            continue

        # If the word is not in the dictionary, add it with its length
        unique_words[word] = len(word)

    # Get the length of the shortest word(s)
    shortest_word_length = min(unique_words.values())

    # Get the shortest unique words using a list comprehension
    shortest_unique_words = [word for word, length in unique_words.items() if length == shortest_word_length]

    return shortest_word_length, shortest_unique_words

def find_longest_unique_words(words: list):
    unique_words = {}

    for word in words:
        # Check if the word is already in the dictionary
        if word in unique_words:
            continue

        # If the word is not in the dictionary, add it with its length
        unique_words[word] = len(word)

    # Get the length of the longest word(s)
    longest_word_length = max(unique_words.values())

    # Get the longest unique words using a list comprehension
    longest_unique_words = [word for word, length in unique_words.items() if length == longest_word_length]

    return longest_word_length, longest_unique_words

    # This function could be further optimized by using a generator expression instead of a list comprehension to filter the dictionary into a list of longest unique words. This would avoid creating a new list in memory, which could be more efficient for very large input lists. With this optimization, the last two lines of the function would look like this:
    
    # longest_unique_words = (word for word, length in unique_words.items() if length == longest_word_length)

    # return longest_word_length, list(longest_unique_words)


# The following alternative version of the above function uses a list instead of a dictionary to keep track of the longest unique words. However, this version is less efficient and also requires the use of a set to remove the duplicate words from the input list.

# def find_longest_unique_words(words: list):
#     longest_word_length = 0
#     longest_unique_words = []

#     # Create a set of all unique words in the input list so as to remove duplicates
#     unique_words = set(words)

#     for word in unique_words:
#         if len(word) > longest_word_length:
#             longest_word_length = len(word)
#             longest_unique_words = [word]
#         elif len(word) == longest_word_length:
#             longest_unique_words.append(word)

#     return longest_word_length, longest_unique_words

def count_word_frequencies(words: list):
    # Loop through list of words to populate dictionary
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    # The above is shorthand for the following
    #
    # for word in words:
    #     if word not in word_frequencies.keys():
    #         word_frequencies[word] = 1
    #     else:
    #         word_frequencies[word] = word_frequencies[word] + 1
    return word_frequencies

# TODO Implement the following functionality to give the user a choice to save the word frequencies to a csv-file

# with open("word_frequencies.csv", "w") as file:
#     # Write header line
#     file.write("Word,Frequency\n")

#     # Loop through dictionary and write key-value pairs to csv
#     for word, frequency in word_frequencies.items():
#         file.write(f"{word},{frequency}\n")
