from Infrastructure.Services.GymService import GymService


class GymsPreProcessingAction:
    GymService = None

    def __init__(self):
        self.GymService = GymService()

    def run(self, lat, lng):
        if self.GymService.has_gym_nearest(lat, lng, 100):
            return 'gymIn100m'
        elif self.GymService.has_gym_nearest(lat, lng, 250):
            return 'gymIn250m'
        elif self.GymService.has_gym_nearest(lat, lng, 500):
            return 'gymIn500m'
        elif self.GymService.has_gym_nearest(lat, lng, 1000):
            return 'gymIn1000m'
        elif self.GymService.has_gym_nearest(lat, lng, 2500):
            return 'gymIn2500m'
        elif self.GymService.has_gym_nearest(lat, lng, 5000):
            return 'gymIn5000m'
        else:
            return 'gymIn+5000m'
