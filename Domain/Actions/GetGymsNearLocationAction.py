from Infrastructure.Services.GymService import GymService


class GetGymsNearLocationAction:
    _GymService = None

    def __init__(self):
        self._GymService = GymService()

    def run(self, lat, lng):
        return self._GymService.get_gyms_near(lat, lng, 500)
