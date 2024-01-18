from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# API Key
api_key = "b1686e27e7a943dfa5e130559233010"

@app.route('/', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        city_name = request.form['city_name']

        # Define the URL with the provided API key and city name
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"

        # Send a GET request to the URL
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return render_template('weather.html', data=data)
        else:
            return "Request failed with status code: " + str(response.status_code)

    return render_template('weather.html')

if __name__ == '__main__':
    app.run()
