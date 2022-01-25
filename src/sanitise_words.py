import re
from string import punctuation

class SanitiseWord:
    def __init__(self):
        pass

    def sanitise_word(self, word):
        valid_word = word.isalpha()
        if not valid_word:
            word = re.sub(r"\'s", "", word)
            word = re.sub(r"\'ve", "", word)
            word = re.sub(r"n\'t", "", word)
            word = re.sub(r"\'re", "", word)
            word = re.sub(r"\'d", "", word)
            word = re.sub(r"\'ll", "", word)
            word = re.sub(f"[{re.escape(punctuation)}]", "", word)
            return word.capitalize()
        
        return word.capitalize()