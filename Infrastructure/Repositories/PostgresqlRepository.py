from psycopg2 import psycopg1


class PostgresqlRepository:
    __ServerIp = "pokeradar-postgresql-dev.sandbox"
    __ServerPort = "5432"
    __conn = None
    __cur = None

    def get_gyms_near(self, lat, lng, distance_meters):
        distance = distance_meters / 100000
        query = "SELECT g.* FROM gyms AS g WHERE ST_Distance(g.position, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) < %s"
        data = (lat, lng, distance)
        self.__connect_to_database()
        self.__cur.execute(query, data)
        response = self.__cur.fetchall()
        self.__close_connection_to_database()
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
        self.__connect_to_database()
        self.__cur.execute(query, data)
        response = self.__cur.fetchone()
        self.__close_connection_to_database()

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
        self.__connect_to_database()
        self.__cur.execute(query, data)
        response = self.__cur.fetchone()
        self.__close_connection_to_database()

        return response

    def get_pokemon_info(self, pokemon_list):
        pokemon_list = pokemon_list.split(',')
        pokemon_list = [int(i) for i in pokemon_list]

        query = "SELECT " \
                "id, " \
                "name " \
                "FROM pokemons " \
                "WHERE id in %(ids)s"
        self.__connect_to_database()
        self.__cur.execute(query, {'ids': tuple(pokemon_list)})
        response = self.__cur.fetchall()
        self.__close_connection_to_database()

        return response

    def __connect_to_database(self):
        self.__conn = psycopg1.connect(
            "host=" + self.__ServerIp + " port=" + self.__ServerPort + " dbname=postgres user=postgres")
        self.__cur = self.__conn.cursor()

    def __close_connection_to_database(self):
        self.__cur.close()
        self.__conn.close()
