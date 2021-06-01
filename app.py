#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request 
from requests import get 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    
    if request.method == 'POST':
        
        degree_symbol = chr(176)
        city = request.form['city']
        state = request.form['state']

        #open weather map api
        url = 'https://api.openweathermap.org/data/2.5/weather?q={},{},us&units=imperial&appid=1490177484e0ac7feb61fca6b2be15b3'.format(city, state)

        # request url
        data = get(url)

        # put data in json format
        weather = data.json()

        # create weather variables from json data
        description = weather['weather'][0]['description']
        icon_id = weather['weather'][0]['icon']
        temp = weather['main']['temp']
        temp = round(int(temp))
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        wind = round(int(wind))
        date = weather['dt']

        return render_template('index.html', city=city, state=state, 
                temp=temp, desc=description, humid=humidity, 
                icon_id=icon_id, wind=wind, degree_symbol=degree_symbol)
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
