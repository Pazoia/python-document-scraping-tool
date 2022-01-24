class SentenceFinder:
    def __init__(self):
        self.sentences_list = []

    def find_sentences_in_data(self, string_with_sentences):
        sentence_builder = []
        for word in string_with_sentences.split():
            if word[-1] != ".":
                sentence_builder.append(f"{word}")
            elif word[-1] == ".":
                sentence_builder.append(f"{word}")
                sentence = " ".join(sentence_builder)
                self.sentences_list.append(sentence)
                sentence_builder.clear()

        return self.sentences_list
