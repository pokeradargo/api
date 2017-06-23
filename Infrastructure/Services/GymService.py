from Infrastructure.Repositories.PostgresqlRepository import PostgresqlRepository


class GymService:
    _PostgresqlRepository = None

    def __init__(self):
        self._PostgresqlRepository = PostgresqlRepository()

    def get_gyms_near(self, lat, lng, distance_meters):
        gyms_collection = self._PostgresqlRepository.get_gyms_near(lat, lng, distance_meters)
        response = {}
        for gym in gyms_collection:
            gym_info = {
                'id': gym[0],
                'lat': str(gym[7]),
                'lng': str(gym[8])
            }
            response[gym[0]] = gym_info

        return response

    def get_gym_nearest(self, lat, lng):
        return self._PostgresqlRepository.get_gym_nearest(lat, lng)
