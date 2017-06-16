from Infrastructure.Services.TemperatureDefinitionService import TemperatureDefinitionService
from Infrastructure.Services.PressureDefinitionService import PressureDefinitionService
from Infrastructure.Services.WindSpeedDefinitionService import WindSpeedDefinitionService
from Infrastructure.Services.WeatherIconDefinitionService import WeatherIconDefinitionService
import pycurl
import io
import json


class WeatherPreProcessingService:
    UrlService = 'https://api.darksky.net/forecast/'
    Token = 'token'

    def pre_processing_weather(self, lat, lng):
        url = self.UrlService + self.Token + '/' + lat + ',' + lng
        print(url)
        buffer = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, buffer.write)
        c.perform()
        c.close()

        body = buffer.getvalue().decode('UTF-8')
        body = json.loads(body)

        temperature = body['currently']['temperature']
        pressure = body['currently']['pressure']
        wind_speed = body['currently']['windSpeed']
        weather_icon = body['currently']['icon']

        temperature = TemperatureDefinitionService.get_temperature_definition(
            float(temperature)
        )
        pressure = PressureDefinitionService.get_pressure_definition(
            float(pressure)
        )
        wind_speed = WindSpeedDefinitionService.get_wind_speed_definition(
            float(wind_speed)
        )
        weather_icon = WeatherIconDefinitionService.get_weather_icon_definition(
            weather_icon
        )
        return {
            'temperature': temperature,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'weather_icon': weather_icon
        }
