from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


def get_random_quote():
    try:
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()
        quote_data = response.json()
        return {
            "content": quote_data['content'],
            "author": quote_data['author']
        }
    except requests.exceptions.RequestException as e:
        return {
            "content": "Ошибка при получении цитаты.",
            "author": ""
        }


@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)


@app.route('/new-quote', methods=['GET'])
def new_quote():
    quote = get_random_quote()
    return jsonify(quote)


if __name__ == '__main__':
    app.run(debug=True)
