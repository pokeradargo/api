from Infrastructure.Repositories.ElasticSearchRepository import ElasticSearchRepository


class PokemonPredictorService:
    __ProbabilityRepository = None

    def __init__(self):
        self.__ProbabilityRepository = ElasticSearchRepository()

    def get_probability(self,
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
        return self.__ProbabilityRepository.get_probability(
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
        )
