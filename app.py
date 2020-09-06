from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    result = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
    countries = result.json()
    return render_template('home.html', countries=countries)


@app.route('/<string:countryName>', methods=['GET'])
def details(countryName):
    response = requests.get(
        f'https://coronavirus-19-api.herokuapp.com/countries/{countryName}')
    case = response.json()
    return render_template('details.html', case=case)


if __name__ == '__main__':
    app.run(debug=True)
