from psycopg2 import psycopg1


class PostgresqlRepository:
    _ServerIp = "pokeradar-postgresql-dev.sandbox"
    _ServerPort = "5432"
    _conn = None
    _cur = None

    def get_gyms_near(self, lat, lng, distance_meters):
        distance = distance_meters / 100000
        query = "SELECT g.* FROM gyms AS g WHERE ST_Distance(g.position, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) < %s"
        data = (lat, lng, distance)
        self._connect_to_database()
        self._cur.execute(query, data)
        response = self._cur.fetchall()
        self._close_connection_to_database()
        return response

    def get_gym_nearest(self, lat, lng):
        query = "SELECT " \
                "   ST_Distance(g.position, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) AS distance," \
                "   g.* " \
                "FROM gyms AS g " \
                "WHERE g.position = (" \
                "   SELECT " \
                "       ST_ClosestPoint(ST_Collect(g2.position)," \
                "       ST_SetSRID(ST_MakePoint(%s, %s), 4326)) " \
                "   FROM gyms AS g2" \
                ")"
        data = (lat, lng, lat, lng)
        self._connect_to_database()
        self._cur.execute(query, data)
        response = self._cur.fetchone()
        self._close_connection_to_database()

        return response

    def get_pokestop_nearest(self, lat, lng):
        query = "SELECT " \
                "   ST_Distance(ps.position, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) AS distance," \
                "   ps.* " \
                "FROM pokestops AS ps " \
                "WHERE ps.position = (" \
                "   SELECT " \
                "       ST_ClosestPoint(ST_Collect(ps2.position)," \
                "       ST_SetSRID(ST_MakePoint(%s, %s), 4326)) " \
                "   FROM pokestops AS ps2" \
                ")"
        data = (lat, lng, lat, lng)
        self._connect_to_database()
        self._cur.execute(query, data)
        response = self._cur.fetchone()
        self._close_connection_to_database()

        return response



    def _connect_to_database(self):
        self._conn = psycopg1.connect("host=" + self._ServerIp + " port=" + self._ServerPort + " dbname=postgres user=postgres")
        self._cur = self._conn.cursor()

    def _close_connection_to_database(self):
        self._cur.close()
        self._conn.close()
