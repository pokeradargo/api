from Infrastructure.Services.LocationService import LocationService
from Domain.Services.ContinentDefinitionService import ContinentDefinitionService


class LocationPreProcessingAction:
    _LocationService = None

    def __init__(self):
        self._LocationService = LocationService()

    def run(self, lat, lng):
        location_data = self._LocationService.get_location_data(lat, lng)

        continent = ContinentDefinitionService.get_continent_definition(location_data['country_code'])

        return {
           'continent': continent
        }
