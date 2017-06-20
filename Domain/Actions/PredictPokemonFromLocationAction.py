from Domain.Actions.Responses.PredictPokemonFromLocationResponse import PredictPokemonFromLocationResponse
from Domain.Actions.WeatherPreProcessingAction import WeatherPreProcessingAction
from Domain.Actions.LocationPreProcessingAction import LocationPreProcessingAction
from Domain.Actions.GymsPreProcessingAction import GymsPreProcessingAction


class PredictPokemonFromLocationAction:
    WeatherPreProcessingAction = None
    LocationPreProcessingAction = None
    GymsPreProcessingAction = None

    def __init__(self):
        self.WeatherPreProcessingAction = WeatherPreProcessingAction()
        self.LocationPreProcessingAction = LocationPreProcessingAction()
        self.GymsPreProcessingAction = GymsPreProcessingAction()

    def run(self, lat, lng):
        # location = self.LocationPreProcessingAction.run(lat, lng)
        gym = self.GymsPreProcessingAction.run(lat, lng)
        weather = self.WeatherPreProcessingAction.run(lat, lng)

        return PredictPokemonFromLocationResponse(
            gym,
            weather['temperature'],
            weather['pressure'],
            weather['wind_speed'],
            weather['weather_icon'],
            {
                "Charmander": "0.4056",
                "Squirtle": "0.2856"
            }
        )
