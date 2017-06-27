from Domain.Actions.Responses.PredictPokemonFromLocationResponse import PredictPokemonFromLocationResponse
from Domain.Actions.WeatherPreProcessingAction import WeatherPreProcessingAction
from Domain.Actions.LocationPreProcessingAction import LocationPreProcessingAction
from Domain.Actions.GymsPreProcessingAction import GymsPreProcessingAction
from Domain.Actions.PokestopsPreProcessingAction import PokestopPreProcessingAction
from Domain.Actions.AppearedTimeDayPreProcessingAction import AppearedTimeDayPreProcessingAction
from Infrastructure.Services.PokemonPredictorService import PokemonPredictorService
from Infrastructure.Services.PokemonInfoService import PokemonInfoService


class PredictPokemonFromLocationAction:
    __WeatherPreProcessingAction = None
    __LocationPreProcessingAction = None
    __GymsPreProcessingAction = None
    __PokestopPreProcessingAction = None
    __AppearedTimeDayPreProcessingAction = None
    __PokemonPredictorService = None
    __PokemonInfoService = None

    def __init__(self):
        self.__WeatherPreProcessingAction = WeatherPreProcessingAction()
        self.__LocationPreProcessingAction = LocationPreProcessingAction()
        self.__GymsPreProcessingAction = GymsPreProcessingAction()
        self.__PokestopPreProcessingAction = PokestopPreProcessingAction()
        self.__AppearedTimeDayPreProcessingAction = AppearedTimeDayPreProcessingAction()
        self.__LocationPreProcessingAction = LocationPreProcessingAction()
        self.__PokemonPredictorService = PokemonPredictorService()
        self.__PokemonInfoService = PokemonInfoService()

    def run(self, lat, lng):
        urbanization = 'urban'
        terrain_type = 'Urban and built-up'
        close_to_water = 'Yes'
        location = self.__LocationPreProcessingAction.run(lat, lng)
        appeared_time_of_day = self.__AppearedTimeDayPreProcessingAction.run(lat, lng)
        pokestop = self.__PokestopPreProcessingAction.run(lat, lng)
        gym = self.__GymsPreProcessingAction.run(lat, lng)
        weather = self.__WeatherPreProcessingAction.run(lat, lng)

        prediction = self.__build_pokemon_predictor_response(
            self.__get_pokemon_prediction(
                urbanization,
                terrain_type,
                close_to_water,
                appeared_time_of_day,
                pokestop,
                gym,
                location['continent'],
                weather['temperature'],
                weather['pressure'],
                weather['wind_speed'],
                weather['weather_icon']
            )
        )

        return PredictPokemonFromLocationResponse(
            urbanization,
            terrain_type,
            close_to_water,
            appeared_time_of_day,
            pokestop,
            gym,
            location['continent'],
            weather['temperature'],
            weather['pressure'],
            weather['wind_speed'],
            weather['weather_icon'],
            prediction
        )

    def __get_pokemon_prediction(self,
                                 urbanization,
                                 terrain_type,
                                 close_to_water,
                                 appeared_time_of_day,
                                 pokestop,
                                 gym,
                                 continent,
                                 temperature,
                                 pressure,
                                 wind_speed,
                                 weather_icon
                                 ):
        return self.__PokemonPredictorService.get_probability(
            urbanization,
            terrain_type,
            close_to_water,
            appeared_time_of_day,
            pokestop,
            gym,
            continent,
            temperature,
            pressure,
            wind_speed,
            weather_icon)

    def __build_pokemon_predictor_response(self, prediction):
        pokemon_response = {}
        if prediction is not None \
                and 'pokemons' in prediction.keys():
            pokemons = self.__get_pokemon_info(prediction['pokemons'])
            for pokemon in pokemons:
                pokemon_response.update({
                    pokemon: prediction['accumulatedprediction']
                })
        return pokemon_response

    def __get_pokemon_info(self, pokemon_list):
        return self.__PokemonInfoService.get_pokemon_names(pokemon_list)
