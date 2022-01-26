class SearchCriteria:
    def __init__(self):
        pass

    def is_long_isogramic_word(self, word):
        """
            An Isogram is a word in which no letter of the alphabet occurs more than once. 
        """
        
        if len(word) < 10:
            return False
        
        lowered_word = word.lower()
        word_chars = list(lowered_word)
        
        for letter in word_chars:
            if lowered_word.count(letter) > 1:
                return False
        
        return True