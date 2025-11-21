# anagrams.py

from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()  # create instance
    
    while True:
        print("\n--- Anagram Checker Menu ---")
        print("1. Choose a word")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ").strip()
    
        if choice == "1":
            word = input("Enter a word to check if it's valid: ").strip()
            
            # Ensure only one word
            if len(word.split()) > 1:
                print("Invalid input. You can only enter ONE word.")
                continue

            # Ensure it's alphabetic
            if not word.isalpha():
                print("Error: Your word must contain only letters.")
                continue
                
            # Check if valid
            if checker.is_valid_word(word):
                print("This is a valid word.")

                anagrams = checker.get_anagrams(word)
                if anagrams:
                    print(f"Anagrams of '{word}': {', '.join(anagrams)}")
                else:
                    print(f"No anagrams found for '{word}'.")
            
            else:
                print(f"'{word}' is not a valid English word.")
        
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid menu choice. Please enter 1 or 2.")
            continue


if __name__ == "__main__":
    main()


