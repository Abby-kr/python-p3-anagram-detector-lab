# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
    
    def match(self,list):
            
        matching_words = []
        word_list = [letter for letter in self.word]
        for word in list:
            anagram = [char for char in word]
            if sorted(word_list) == sorted(anagram):
                matching_words.append(word)

        if len(matching_words) == 0:
            return []
        else:
            return matching_words
            

