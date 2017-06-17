from Infrastructure.Services.CurlService import CurlService


class WeatherPreProcessingService:
    UrlService = 'https://api.darksky.net/forecast/'
    Token = 'token'
    CurlService = None

    def __init__(self):
        self.CurlService = CurlService()

    def get_weather_data(self, lat, lng):
        url = self.UrlService + self.Token + '/' + lat + ',' + lng
        body = self.CurlService.get_json(url)

        temperature = body['currently']['temperature']
        pressure = body['currently']['pressure']
        wind_speed = body['currently']['windSpeed']
        weather_icon = body['currently']['icon']

        return {
            'temperature': temperature,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'weather_icon': weather_icon
        }
