from Domain.Actions.Responses.PredictPokemonFromLocationResponse import PredictPokemonFromLocationResponse
from Domain.Actions.WeatherPreProcessingAction import WeatherPreProcessingAction


class PredictPokemonFromLocationAction:
    WeatherPreProcessingAction = None

    def __init__(self):
        self.WeatherPreProcessingAction = WeatherPreProcessingAction()

    def run(self, lat, lng):
        weather = self.WeatherPreProcessingAction.run(lat, lng)

        return PredictPokemonFromLocationResponse(
            weather['temperature'],
            weather['pressure'],
            weather['wind_speed'],
            weather['weather_icon']
        )
