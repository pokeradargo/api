from Domain.Actions.Responses.PredictPokemonFromLocationResponse import PredictPokemonFromLocationResponse
from Domain.Actions.WeatherPreProcessingAction import WeatherPreProcessingAction
from Domain.Actions.LocationPreProcessingAction import LocationPreProcessingAction
from Domain.Actions.GymsPreProcessingAction import GymsPreProcessingAction
from Domain.Actions.PokestopsPreProcessingAction import PokestopPreProcessingAction
from Domain.Actions.AppearedTimeDayPreProcessingAction import AppearedTimeDayPreProcessingAction


class PredictPokemonFromLocationAction:
    _WeatherPreProcessingAction = None
    _LocationPreProcessingAction = None
    _GymsPreProcessingAction = None
    _PokestopPreProcessingAction = None
    _AppearedTimeDayPreProcessingAction = None

    def __init__(self):
        self._WeatherPreProcessingAction = WeatherPreProcessingAction()
        self._LocationPreProcessingAction = LocationPreProcessingAction()
        self._GymsPreProcessingAction = GymsPreProcessingAction()
        self._PokestopPreProcessingAction = PokestopPreProcessingAction()
        self._AppearedTimeDayPreProcessingAction = AppearedTimeDayPreProcessingAction()
        self._LocationPreProcessingAction = LocationPreProcessingAction()

    def run(self, lat, lng):
        location = self._LocationPreProcessingAction.run(lat, lng)
        appeared_time_of_day = self._AppearedTimeDayPreProcessingAction.run(lat, lng)
        pokestop = self._PokestopPreProcessingAction.run(lat, lng)
        gym = self._GymsPreProcessingAction.run(lat, lng)
        weather = self._WeatherPreProcessingAction.run(lat, lng)

        return PredictPokemonFromLocationResponse(
            appeared_time_of_day,
            pokestop,
            gym,
            location['continent'],
            weather['temperature'],
            weather['pressure'],
            weather['wind_speed'],
            weather['weather_icon'],
            {
                "Charmander": "0.4056",
                "Squirtle": "0.2856"
            }
        )
