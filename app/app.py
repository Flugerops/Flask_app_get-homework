from flask import Flask, request, render_template
import requests
from dotenv import load_dotenv
from os import getenv


load_dotenv()
key = getenv("key")

app = Flask(__name__)


@app.get("/")
def index():
    popular_cities = [
        "Kyiv",
        "Odessa",
        "Lviv",
        "Dnipro",
        "Kharkiv"
    ]
    return render_template("index.html", popular_cities=popular_cities)


@app.post("/weather")
def show_weather():
    city = request.form['city']
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric").json()
    weather_data = {
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "wind_speed": response["wind"]["speed"],
    }
    return render_template('weather_data.html', city=city, weather_data=weather_data)