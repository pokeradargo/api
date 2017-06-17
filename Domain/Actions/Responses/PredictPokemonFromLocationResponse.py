class PredictPokemonFromLocationResponse:
    Temperature = ''
    Pressure = ''
    WindSpeed = ''
    WeatherIcon = ''
    Predictions = ''

    def __init__(
            self,
            temperature,
            pressure,
            wind_speed,
            weather_icon,
            predictions
    ):
        self.Temperature = temperature
        self.Pressure = pressure
        self.WindSpeed = wind_speed
        self.WeatherIcon = weather_icon
        self.Predictions = predictions

    def get_response(self):
        return {
            "temperature": self.Temperature,
            "pressure": self.Pressure,
            "wind_speed": self.WindSpeed,
            "weather_icon": self.WeatherIcon,
            "predictions": self.Predictions
        }
