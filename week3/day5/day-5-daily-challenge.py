# Exercise: Text Analysis and Modification
import string
import re

# ---------------------------
# Part I: Analyzing Text
# ---------------------------

class Text:
    def __init__(self, text):
        self.text = text  # Store the text

    # Step 2: Count occurrences of a specific word
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' was not found."
        return count

    # Step 3: Find the most common word
    def most_common_word(self):
        words = self.text.split()
        frequency = {}
        for word in words:
            word_lower = word.lower()  # normalize to lowercase
            frequency[word_lower] = frequency.get(word_lower, 0) + 1
        if not frequency:
            return None
        most_common = max(frequency, key=frequency.get)
        return most_common

    # Step 4: Get unique words
    def unique_words(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)

    # Step 5: Create instance from file
    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()
                return cls(content)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


# ---------------------------
# Part II: Text Modification
# ---------------------------

class TextModification(Text):
    # Step 7: Remove punctuation
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    # Step 8: Remove stop words
    def remove_stop_words(self):
        # Common English stop words
        stop_words = {
            "a", "an", "and", "the", "is", "in", "it", "of", "or", "to", "for",
            "on", "with", "as", "by", "at", "from", "that", "this", "be", "are"
        }
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        self.text = " ".join(filtered_words)
        return self.text

    # Step 9: Remove special characters using regex
    def remove_special_characters(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)  # keep letters, numbers, spaces
        return self.text


# ---------------------------
# Example Usage
# ---------------------------

if __name__ == "__main__":
    # Example: create Text instance from string
    sample_text = "Hello, hello! This is an example. Let's analyze this text."
    text_obj = Text(sample_text)
    
    print("Word frequency for 'hello':", text_obj.word_frequency("hello"))
    print("Most common word:", text_obj.most_common_word())
    print("Unique words:", text_obj.unique_words())

    # Example: create Text instance from a file
    # file_text = Text.from_file("example.txt")
    # if file_text:
    #     print(file_text.text)

    # Example: Text modification
    mod_text = TextModification(sample_text)
    print("Original text:", mod_text.text)
    print("Remove punctuation:", mod_text.remove_punctuation())
    print("Remove stop words:", mod_text.remove_stop_words())
    print("Remove special characters:", mod_text.remove_special_characters())
