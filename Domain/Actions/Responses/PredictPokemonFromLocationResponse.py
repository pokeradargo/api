class PredictPokemonFromLocationResponse:
    GymDistance = ''
    Temperature = ''
    Pressure = ''
    WindSpeed = ''
    WeatherIcon = ''
    Predictions = ''

    def __init__(
            self,
            gym_distance,
            temperature,
            pressure,
            wind_speed,
            weather_icon,
            predictions
    ):
        self.GymDistance = gym_distance
        self.Temperature = temperature
        self.Pressure = pressure
        self.WindSpeed = wind_speed
        self.WeatherIcon = weather_icon
        self.Predictions = predictions

    def get_response(self):
        return {
            "gym_distance": self.GymDistance,
            "temperature": self.Temperature,
            "pressure": self.Pressure,
            "wind_speed": self.WindSpeed,
            "weather_icon": self.WeatherIcon,
            "predictions": self.Predictions
        }
