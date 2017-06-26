from Infrastructure.Services.PokeStopService import PokeStopService
from Domain.Services.PokestopDefinitionService import PokestopDefinitionService

class PokestopPreProcessingAction:
    _PokestopService = None

    def __init__(self):
        self._PokestopService = PokeStopService()

    def run(self, lat, lng):
        distance = None
        pokestop_nearest = self._PokestopService.get_pokestop_nearest(lat, lng)

        if pokestop_nearest is not None:
            # convert distance to meters
            distance = float(pokestop_nearest[0]) * 100000

        return PokestopDefinitionService.get_distance_definition(distance)
