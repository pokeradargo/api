from Infrastructure.Services.GymService import GymService


class GymsPreProcessingAction:
    GymService = None

    def __init__(self):
        self.GymService = GymService()

    def run(self, lat, lng):
        distance = None
        gym_nearest = self.GymService.get_gym_nearest(lat, lng)

        if gym_nearest is not None:
            # convert distance to meters
            distance = float(gym_nearest[0]) * 100000

        if distance is not None and distance <= 100:
            return 'gymIn100m'
        elif distance is not None and distance <= 250:
            return 'gymIn250m'
        elif distance is not None and distance <= 500:
            return 'gymIn500m'
        elif distance is not None and distance <= 1000:
            return 'gymIn1000m'
        elif distance is not None and distance <= 2500:
            return 'gymIn2500m'
        elif distance is not None and distance <= 5000:
            return 'gymIn5000m'
        else:
            return 'gymIn+5000m'
