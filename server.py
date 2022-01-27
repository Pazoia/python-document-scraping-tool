from flask import Flask
from src.app import App

app = Flask(__name__)

@app.route("/words")
def words():
    results = App()
    return results.new_app()


if __name__ == "__main__":
    app.run(debug=True)
