from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)                                       # create Flask web app instance


@app.route('/', methods = ['GET', 'POST'])                  # define route for root url to handel get and post requests
def index():
    data = None                                             # initialize data variable to none
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city, state, country)            # call get weather function 
    return render_template('index.html', data=data)         # render the index.html template    

if __name__ == '__main__':                                  
    app.run(debug = True)                                   # run Flask in debug mode