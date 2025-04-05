from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker() #creates instance
    
    while True:
        print("\n--- Anagram Checker Menu ---")
        print("1. Choose a word")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ").strip() #removes all whitespaces
    
        if choice == "1":
            word = input("Enter a word to check if it's valid: ").strip()
            
            word_count = len(word.split()) #split splits the whitespaces
            if word_count > 1:
                print(f"Invalid input. You can only enter one word, not {word_count} words")
                continue

            if not word.isalpha(): #isalpha makes sure all characters are letters
                print("You can only enter one word containing letters")
                continue
                
            if checker.is_valid_word(word): #pulls from is_valid_word method in anagram_checker
                print("This is a valid word.")

                anagrams = checker.get_anagrams(word) #pulls anagrams from method in anagram_checker from list
                if anagrams:
                    print(f"Anagrams of '{word}': {', '.join(anagrams)}")
                    break #If all true, put break after last true part

                else:
                    print(f"No anagrams found for '{word}'.")
            else:
                print(f"'{word}' is not a valid word.")
        
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Not a valid answer. Please check the menu")
            break
    


if __name__ == "__main__":
    main()

