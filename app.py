from src.data_extraction import DataExtraction
from src.convert_data_into_list_of_sentences import SentenceFinder

from pathlib import Path

class App:
    def __init__(self):
        self.files_folder = Path("src/data-files/")
        self.filepath = list(self.files_folder.glob("*.txt"))

    def new_app(self):
        self.data = DataExtraction()
        self.sentence_filter = SentenceFinder()

        for file in self.filepath:
            file_data = self.data.get_data_from_file(file)
            sentences = self.sentence_filter.find_sentences_in_data(file_data)
            for sentence in sentences:
                for word in sentence.split():
                    if word == "same-sex":
                        print(f"The word {word} is in sentence:\n{sentence}")

app = App()
app.new_app()