from src.data_extraction import DataExtraction
from src.sentence_filter import SentenceFinder
from src.search_criteria import SearchCriteria
from src.sanitise_words import SanitiseWord

from pathlib import Path

class WordSearch:
    def __init__(self):
        self.files_folder = Path("src/data-files/")
        self.filepath = list(self.files_folder.glob("*.txt"))
        self.data = DataExtraction()
        self.sentence_filter = SentenceFinder()
        self.is_isogram = SearchCriteria()
        self.sanitise_word = SanitiseWord()
        self.results = {}

    def find_word(self, sentence, filename):
        for word in sentence.split():
            sanitised_word = self.sanitise_word.sanitise_word(word)
            if self.is_isogram.is_long_isogramic_word(sanitised_word):
                self.results[sanitised_word] = {"word_count": 1, "file": filename, "sentence": sentence}
    
    def search(self):
        for file in self.filepath:
            file_data = self.data.get_data_from_file(file)
            sentences = self.sentence_filter.find_sentences_in_data(file_data)
            
            list(map(lambda sentence: self.find_word(sentence, file.name), sentences))
        
        return self.results
