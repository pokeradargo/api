from Domain.Services.PressureDefinitionService import PressureDefinitionService
from Domain.Services.TemperatureDefinitionService import TemperatureDefinitionService
from Domain.Services.WeatherIconDefinitionService import WeatherIconDefinitionService
from Domain.Services.WindSpeedDefinitionService import WindSpeedDefinitionService

from Infrastructure.Services.WeatherPreProcessingService import WeatherPreProcessingService


class WeatherPreProcessingAction:
    WeatherPreProcessingService = None

    def __init__(self):
        self.WeatherPreProcessingService = WeatherPreProcessingService()

    def run(self, lat, lng):
        weather_data = self.WeatherPreProcessingService.get_weather_data(lat, lng)

        temperature = TemperatureDefinitionService.get_temperature_definition(
            float(weather_data['temperature'])
        )
        pressure = PressureDefinitionService.get_pressure_definition(
            float(weather_data['pressure'])
        )
        wind_speed = WindSpeedDefinitionService.get_wind_speed_definition(
            float(weather_data['wind_speed'])
        )
        weather_icon = WeatherIconDefinitionService.get_weather_icon_definition(
            weather_data['weather_icon']
        )
        return {
            'temperature': temperature,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'weather_icon': weather_icon
        }
