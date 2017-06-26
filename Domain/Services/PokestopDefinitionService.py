class PokestopDefinitionService:
    @staticmethod
    def get_distance_definition(distance):
        if distance is not None and distance <= 100:
            return 'pokestopIn100m'
        elif distance is not None and distance <= 250:
            return 'pokestopIn250m'
        elif distance is not None and distance <= 500:
            return 'pokestopIn500m'
        elif distance is not None and distance <= 1000:
            return 'pokestopIn1000m'
        elif distance is not None and distance <= 2500:
            return 'pokestopIn2500m'
        elif distance is not None and distance <= 5000:
            return 'pokestopIn5000m'
        else:
            return 'pokestopIn+5000m'
