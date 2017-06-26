class GymDefinitionService:
    @staticmethod
    def get_distance_definition(distance):
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
