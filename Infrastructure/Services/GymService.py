from Infrastructure.Repositories.PostgresqlRepository import PostgresqlRepository


class GymService:
    PostgresqlRepository = None

    def __init__(self):
        self.PostgresqlRepository = PostgresqlRepository()

    def get_gyms_near(self, lat, lng, distance_meters):
        gyms_collection = self.PostgresqlRepository.get_gyms_near(lat, lng, distance_meters)
        response = {}
        for gym in gyms_collection:
            gym_info = {
                'id': gym[0],
                'lat': str(gym[7]),
                'lng': str(gym[8])
            }
            response[gym[0]] = gym_info

        return response

    def has_gym_nearest(self, lat, lng, distance_meters):
        gym = self.PostgresqlRepository.get_gym_nearest(lat, lng, distance_meters)
        return gym is not None
