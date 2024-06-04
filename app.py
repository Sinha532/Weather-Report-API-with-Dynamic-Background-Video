from flask import Flask, render_template, request,jsonify
import requests

app=Flask(__name__)

WEATHER_API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "7802a45c4c10dbfc3d999bced50cc631"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods=["POST"])
def get_weather():
    search_query=request.form['search_query']
    params = {
        "q": search_query,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    response = requests.get(WEATHER_API_ENDPOINT, params=params)
    weather_data = response.json()
    #print(weather_data)
    status=weather_data["weather"][0]["main"].capitalize()
    if status=="Clouds":
        background_image='cloudy.mp4'
    elif status=="Haze":
        background_image='haze.mp4'
    elif status=="Sunny":
        background_image='sunny.mp4'
    elif status=="Snow":
        background_image="snow.mp4"
    else:
        background_image="video.mp4"

    
    
    return render_template('final.html',
                           title=weather_data['name'],
                           status=weather_data["weather"][0]["main"].capitalize(),
                           temp=f"{weather_data['main']['temp']:.1f}",
                           feels_like=f"{weather_data['main']['feels_like']:.1f}",background_image=background_image)

if __name__=="__main__":
    app.run()
