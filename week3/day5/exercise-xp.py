# Exercise 1 – Random Sentence Generator
import random

class Random():
    def __init__(self):
        with open('sowpods.txt', 'r') as file:
            self.word_list = [line.strip() for line in file] #reads each line

    def get_words_from_file(self, word):
        return words in self.word_list

    def get_random_sentence(self, length):
        if length <= 0:
            return "Length must be greater than 0." #ensures valid length
        
        random_words = random.choices(self.word_list,k=length) #randomly selects choice of words to fit length

        return ' '.join(random_words) #' '.join() makes it a sentence

def main(): #does not need self
    print("The program generates a random sentence from a list of words. The user is asked how long the sentence should be and then the generated sentence is printed.")

    try:
        user_sentence = int(input("Enter how long you would like the sentence to be as a number between 2-20: "))
        if user_sentence <2 or user_sentence >20:
            print(f"{user_sentence} is not a valid input.")
                
        else:
            random_instance = Random()
            random_sentence = random_instance.get_random_sentence(user_sentence).lower() #adding .lower() at calling converts all words to lower case in output
            print(random_sentence)
            
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()