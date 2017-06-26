class PredictPokemonFromLocationResponse:
    AppearedTimeOfDay = ''
    PokestopDistance = ''
    GymDistance = ''
    Temperature = ''
    Pressure = ''
    WindSpeed = ''
    WeatherIcon = ''
    Predictions = ''

    def __init__(
            self,
            appeared_time_of_day,
            pokestop_distance,
            gym_distance,
            temperature,
            pressure,
            wind_speed,
            weather_icon,
            predictions
    ):
        self.AppearedTimeOfDay = appeared_time_of_day
        self.PokestopDistance = pokestop_distance
        self.GymDistance = gym_distance
        self.Temperature = temperature
        self.Pressure = pressure
        self.WindSpeed = wind_speed
        self.WeatherIcon = weather_icon
        self.Predictions = predictions

    def get_response(self):
        return {
            'appeared_time_of_day': self.AppearedTimeOfDay,
            'poke_stop_distance': self.PokestopDistance,
            'gym_distance': self.GymDistance,
            'temperature': self.Temperature,
            'pressure': self.Pressure,
            'wind_speed': self.WindSpeed,
            'weather_icon': self.WeatherIcon,
            'predictions': self.Predictions
        }
