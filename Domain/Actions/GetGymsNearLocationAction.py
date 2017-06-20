from Infrastructure.Services.GymService import GymService


class GetGymsNearLocationAction:
    GymService = None

    def __init__(self):
        self.GymService = GymService()

    def run(self, lat, lng):
        return self.GymService.get_gyms_near(lat, lng, 500)
