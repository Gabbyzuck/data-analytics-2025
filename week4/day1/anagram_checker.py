# anagram_checker.py

class AnagramChecker:
    def __init__(self, word_file="sowpods.txt"):
        try:
            with open(word_file, "r") as file:
                self.word_list = {line.strip().lower() for line in file}
        except FileNotFoundError:
            raise Exception(f"Error: The file '{word_file}' was not found.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        word = word.lower()
        return [
            w for w in self.word_list
            if w != word and self.is_anagram(word, w)
        ]

