from Domain.Actions.PredictPokemonFromLocationAction import PredictPokemonFromLocationAction
from flask import Flask, json, request
app = Flask(__name__)


@app.route("/", methods=['GET'])
def mail():
    lat = request.args.get('lat', '')
    lng = request.args.get('lng', '')
    if (lat == '') or (lng == ''):
        return "Please Indicate a latitude and longitude in url 'http://localhost:5000/?lat=41.3929909&lng=2.1575654'"

    predict_pokemon_from_location_action = PredictPokemonFromLocationAction()
    response_action = predict_pokemon_from_location_action.run(lat, lng)

    response = format_response(lat, lng, response_action.get_response())

    return response


def format_response(lat, lng, response):
    data_response = {
        "input": {
            "lat": lat,
            "lng": lng,
            "urbanization": "urban",
            "terrain_type": "Urban and built-up",
            "close_to_water": "Yes",
            "poke_stop_distance": "pokestopIn250m",
            "gym_distance": "gymIn500m",
            "continent": "America",
            "appeared_day_of_week": "dummy_day",
            "appeared_time_of_day": "night",
            "temperature": response['temperature'],
            "pressure": response['pressure'],
            "wind_speed": response['wind_speed'],
            "weather_icon": response['weather_icon']
        },
        "output": {
            **response['predictions']
        }
    }
    response = app.response_class(
        response=json.dumps(data_response),
        status=200,
        mimetype='application/json'
    )
    return response