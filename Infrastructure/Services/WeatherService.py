from Infrastructure.Services.CurlService import CurlService


class WeatherService:
    _UrlService = 'https://api.darksky.net/forecast/'
    _Token = 'token'
    _CurlService = None

    def __init__(self):
        self._CurlService = CurlService()

    def get_weather_data(self, lat, lng):
        url = self._UrlService + self._Token + '/' + lat + ',' + lng
        body = self._CurlService.get_json(url)

        temperature = body['currently']['temperature']
        # Convert degrees Fahrenheit temperature to degrees Celsius:
        temperature = (temperature - 32) * 5 / 9
        pressure = body['currently']['pressure']
        wind_speed = body['currently']['windSpeed']
        weather_icon = body['currently']['icon']

        return {
            'temperature': temperature,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'weather_icon': weather_icon
        }
