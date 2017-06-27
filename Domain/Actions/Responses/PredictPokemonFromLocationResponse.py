class PredictPokemonFromLocationResponse:
    Urbanization = ''
    TerrainType = ''
    CloseToWater = ''
    AppearedTimeOfDay = ''
    PokestopDistance = ''
    GymDistance = ''
    Continent = ''
    Temperature = ''
    Pressure = ''
    WindSpeed = ''
    WeatherIcon = ''
    Predictions = ''

    def __init__(
            self,
            urbanization,
            terrain_type,
            close_to_water,
            appeared_time_of_day,
            pokestop_distance,
            gym_distance,
            continent,
            temperature,
            pressure,
            wind_speed,
            weather_icon,
            predictions
    ):
        self.Urbanization = urbanization
        self.TerrainType = terrain_type
        self.CloseToWater = close_to_water
        self.AppearedTimeOfDay = appeared_time_of_day
        self.PokestopDistance = pokestop_distance
        self.GymDistance = gym_distance
        self.Continent = continent
        self.Temperature = temperature
        self.Pressure = pressure
        self.WindSpeed = wind_speed
        self.WeatherIcon = weather_icon
        self.Predictions = predictions

    def get_response(self):
        return {
            'urbanization': self.Urbanization,
            'terrain_type': self.TerrainType,
            'close_to_water': self.CloseToWater,
            'appeared_time_of_day': self.AppearedTimeOfDay,
            'poke_stop_distance': self.PokestopDistance,
            'gym_distance': self.GymDistance,
            'continent': self.Continent,
            'temperature': self.Temperature,
            'pressure': self.Pressure,
            'wind_speed': self.WindSpeed,
            'weather_icon': self.WeatherIcon,
            'predictions': self.Predictions
        }
