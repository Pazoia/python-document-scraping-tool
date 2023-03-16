from flask import Flask

from src.word_search import WordSearch

app = Flask(__name__)

word_search = WordSearch()

@app.route("/words", methods=["GET"])
def words():
    return word_search.search()

if __name__ == "__main__":
    app.run(debug=True)
