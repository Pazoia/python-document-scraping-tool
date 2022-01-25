import re
from string import punctuation

class SanitiseWord:
    def __init__(self):
        self.sanitised_word = ""

    def sanitise_word(self, word):
        valid_word = word.isalpha()
        
        if not valid_word:
            word = re.sub(r"\-", " ", word)
            word = re.sub(r"\'s", "", word)
            word = re.sub(r"\'ve", "", word)
            word = re.sub(r"\'t", "", word)
            word = re.sub(r"\'re", "", word)
            word = re.sub(r"\'d", "", word)
            word = re.sub(r"\'ll", "", word)
            word = re.sub(f"[{re.escape(punctuation)}]", "", word)
            self.sanitised_word = word
        
        self.sanitised_word = word
        return self.sanitised_word.capitalize()