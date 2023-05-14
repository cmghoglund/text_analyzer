import functions

def main():
    """Main function that runs the program."""

    print()
    description = f"This program can be used to analyze text in various ways."
    print(description)
    print("■" * len(description))

    while True:
        print("\nYou can either:")
        choice = input("\n1. Type or paste some text below; or\n2. Provide a text-file to analyze.\n\n-> ")

        if choice == "1":
            while True:
                text = input("\nEnter some text to analyze and press Enter/Return:\n\n")
                if text == "":
                    print("You have to enter some text in order to proceed.")
                else:
                    break
            break
        elif choice == "2":
            filename = input("\nPlease enter the filename of a textfile to analyze (for example, article.txt).\nIf you don't provide a filename and just press Enter/Return, the program will provide a default text for you to analyze.\n\nFilename: ")
            text = functions.open_file(filename)
            break
        else:
            print("Invalid choice. Please choose either 1 or 2.")

    cleaned_text = functions.clean_text(text)
    words = cleaned_text.split()
    unique_words = functions.remove_duplicate_words(words)

    while True:
        prompt = "■ Choose a command: ■"
        print()
        print("■" * len(prompt))
        print(prompt)
        print("■" * len(prompt))

        commands = [
            "Find first word",          #  1 #
            "Find last word",           #  2 #
            "Find first character",     #  3 #
            "Find last character",      #  4 #
            "Count total words",        #  5 #
            "Count total characters",   #  6 #
            "Find words of length",     #  7 #
            "Find words starting with", #  8 #
            "Find words ending with",   #  9 #
            "Choose random word",       # 10 #
            "Find palindromes",         # 11 #
            "Find shortest words",      # 12 #
            "Find longest words",       # 13 #
            "Count word frequencies",   # 14 #
            "Exit",                     # 15 #
        ]

        for number, command in enumerate(commands):
            print(f"\n{number + 1:>2}. {command}", end="")
        command = input("\n\n-> ")
        print()

        if command == "1":
            print(f"The first word in the text is: {functions.find_first_word(words)}")
        elif command == "2":
            print(f"The last word in the text is: {functions.find_last_word(words)}")
        elif command == "3":
            print(f"The first character in the text is: {functions.find_first_character(text)}")
        elif command == "4":
            print(f"The last character in the text is: {functions.find_last_character(text)}")
        elif command == "5":
            print(f"The total number of words in the text is: {functions.count_total_words(words)}")
        elif command == "6":
            print(f"The total number of characters in the text is: {functions.count_total_characters(text)}")
        elif command == "7":
            word_length = int(input("Enter length of words to find: "))
            result = functions.find_words_of_length(word_length, unique_words)
            if result == []:
                print(f"\nSorry, there are no words of length {word_length} in the text.")
            else:
                print(f"\nThe following words of length {word_length} were found in the text: ", end="")
                functions.print_words(result)
        elif command == "8":
            letter = input("Enter first letter of words to find: ").lower()
            result = functions.find_words_starting_with(letter, unique_words)
            if result == []:
                print(f"\nSorry, there are no words starting with the letter \"{letter}\" in the text.")
            else:
                print(f"\nThe following words starting with the letter \"{letter}\" were found in the text: ", end="")
                functions.print_words(result)
        elif command == "9":
            letter = input("Enter last letter of words to find: ").lower()
            result = functions.find_words_ending_with(letter, unique_words)
            if result == []:
                print(f"\nSorry, there are no words ending with the letter \"{letter}\" in the text.")
            else:
                print(f"\nThe following words ending with the letter \"{letter}\" were found in the text: ", end="")
                functions.print_words(result)
        elif command == "10":
            print(f"Here's a random word from the text: {functions.choose_random_word(unique_words)}")
        elif command == "11":
            palindromes = functions.find_palindromes(unique_words)
            if palindromes == []:
                print("Sorry, there are no palindromes in the text.")
            else:
                print("The following palindromes were found in the text: ", end="")
                functions.print_words(palindromes)
                print(f"\nNOTE: Only palindromes with 2 or more characters are included in this count.")
        elif command == "12":
            shortest_word_length, shortest_unique_words = functions.find_shortest_unique_words(words)
            if len(shortest_unique_words) == 1:
                print(f"The shortest word in the text has a length of {shortest_word_length} and is: ", end="")
            else:
                print(f"The shortest words in the text have a length of {shortest_word_length} and include the following: ", end="")
            functions.print_words(shortest_unique_words)
        elif command == "13":
            longest_word_length, longest_unique_words = functions.find_longest_unique_words(words)
            if len(longest_unique_words) == 1:
                print(f"The longest word in the text has a length of {longest_word_length} and is: ", end="")
            else:
                print(f"The longest words in the text have a length of {longest_word_length} and include the following: ", end="")
            functions.print_words(longest_unique_words)
        elif command == "14":
            word_frequencies = functions.count_word_frequencies(sorted(words))
            for word, frequency in word_frequencies.items():
                print(f"\t{word}: {frequency}")
        elif command == "15":
            # \U0001F480 stands for the skull emoji.
            print("\U0001F480\U0001F480\U0001F480 Exiting program. \U0001F480\U0001F480\U0001F480\n")
            break
        else:
            print(f"Invalid command. Please choose a number from 1 to {len(commands)}.")

if __name__ == "__main__":
    main()
