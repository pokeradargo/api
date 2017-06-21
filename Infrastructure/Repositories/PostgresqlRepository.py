from psycopg2 import psycopg1


class PostgresqlRepository:
    ServerIp = "pokeradar-postgresql-dev.sandbox"
    ServerPort = "5432"
    conn = None
    cur = None

    def connect_to_database(self):
        self.conn = psycopg1.connect("host=" + self.ServerIp + " port=" + self.ServerPort + " dbname=postgres user=postgres")
        self.cur = self.conn.cursor()

    def close_connection_to_database(self):
        self.cur.close()
        self.conn.close()

    def get_gyms_near(self, lat, lng, distance_meters):
        distance = distance_meters / 100000
        query = "SELECT g.* FROM gyms AS g WHERE ST_Distance(g.position, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) < %s"
        data = (lat, lng, distance)
        self.connect_to_database()
        self.cur.execute(query, data)
        response = self.cur.fetchall()
        self.close_connection_to_database()
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
        self.connect_to_database()
        self.cur.execute(query, data)
        response = self.cur.fetchone()
        self.close_connection_to_database()

        return response
