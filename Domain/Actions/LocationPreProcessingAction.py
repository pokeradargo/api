from Infrastructure.Services.LocationService import LocationService
from Domain.Services.ContinentDefinitionService import ContinentDefinitionService


class LocationPreProcessingAction:
    _LocationService = None

    def __init__(self):
        self._LocationService = LocationService()

    def run(self, lat, lng):
        location_data = self._LocationService.get_location_data(lat, lng)

        continent = None
        if location_data['country_code'] is not None:
            continent = location_data['country_code']
            continent = continent.upper()
            continent = ContinentDefinitionService.get_continent_definition(continent)

        return {
           'continent': continent
        }
