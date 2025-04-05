class AnagramChecker:
    def __init__(self):
        # Load the word list from the file
        with open("sowpods.txt", "r") as file:
            self.word_list = {line.strip().upper() for line in file}

    # Check if the word is valid by verifying its presence in the word list
    def is_valid_word(self, word):
        return word.upper() in self.word_list

    # Check if two words are anagrams
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    # Get all anagrams of a word from the word list
    def get_anagrams(self, word):
        word = word.lower()
        return [
            potential_word
            for potential_word in self.word_list
            if self.is_anagram(word, potential_word) and word != potential_word
        ]


# Example usage
if __name__ == "__main__":
    checker = AnagramChecker()
    word = "CALL"
    if checker.is_valid_word(word):
        print(f"'{word}' is a valid word.")
        anagrams = checker.get_anagrams(word)
        print(f"Anagrams of '{word}': {anagrams}")
    else:
        print(f"'{word}' is not a valid word.")