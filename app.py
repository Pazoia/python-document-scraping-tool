from src.data_extraction import DataExtraction
from src.sentence_filter import SentenceFinder
from src.word_search_functions import WordSearchFunctions
from src.sanitise_words import SanitiseWord

from pathlib import Path

class App:
    def __init__(self):
        self.files_folder = Path("src/data-files/")
        self.filepath = list(self.files_folder.glob("*.txt"))
        self.results = {}

    def new_app(self):
        self.data = DataExtraction()
        self.sentence_filter = SentenceFinder()
        self.is_isogram = WordSearchFunctions()
        self.sanitise_word = SanitiseWord()

        for file in self.filepath:
            file_data = self.data.get_data_from_file(file)
            sentences = self.sentence_filter.find_sentences_in_data(file_data)
            for sentence in sentences:
                for word in sentence.split():
                    sanitised_word = self.sanitise_word.sanitise_word(word)
                    if self.is_isogram.is_long_isogramic_word(sanitised_word):
                        self.results[word] = {"word_count": 1, "file": file.name, "sentence": sentence}
    
        for key, value in self.results.items():
            print(key)
            print(value)

app = App()
app.new_app()