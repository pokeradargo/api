from Infrastructure.Repositories.PostgresqlRepository import PostgresqlRepository


class PokeStopService:
    _PostgresqlRepository = None

    def __init__(self):
        self._PostgresqlRepository = PostgresqlRepository()

    def get_pokestop_nearest(self, lat, lng):
        return self._PostgresqlRepository.get_pokestop_nearest(lat, lng)
