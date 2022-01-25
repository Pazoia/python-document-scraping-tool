from nltk.tokenize import sent_tokenize

class SentenceFinder:
    def __init__(self):
        pass

    def find_sentences_in_data(self, string_with_sentences):
        if type(string_with_sentences) != str:
            raise Exception("Invalid data type!")
        
        sentences = sent_tokenize(string_with_sentences)

        return sentences
