class DataExtraction:
    def __init__(self):
        pass

    def get_data_from_file(self, filepath):
        with open(filepath, "r") as data:
            return data.read()