from Infrastructure.Services.GymService import GymService
from Domain.Services.GymDefinitionService import GymDefinitionService


class GymsPreProcessingAction:
    _GymService = None

    def __init__(self):
        self._GymService = GymService()

    def run(self, lat, lng):
        distance = None
        gym_nearest = self._GymService.get_gym_nearest(lat, lng)

        if gym_nearest is not None:
            # convert distance to meters
            distance = float(gym_nearest[0]) * 100000

        return GymDefinitionService.get_distance_definition(distance)
