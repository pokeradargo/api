class PredictPokemonFromLocationResponse:
    Temperature = ''
    Pressure = ''
    WindSpeed = ''
    WeatherIcon = ''

    def __init__(
            self,
            temperature,
            pressure,
            wind_speed,
            weather_icon
    ):
        self.Temperature = temperature
        self.Pressure = pressure
        self.WindSpeed = wind_speed
        self.WeatherIcon = weather_icon

    def get_response(self):
        return {
           "temperature": self.Temperature,
           "pressure": self.Pressure,
           "wind_speed": self.WindSpeed,
           "weather_icon": self.WeatherIcon
        }
