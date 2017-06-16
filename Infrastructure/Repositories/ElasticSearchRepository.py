from elasticsearch import Elasticsearch


class ElasticSearchRepository:
    ServerIp = "pokeradar-elastic-master-dev.sandbox"
    ServerPort = 9200

    def connect_to_database(self):
        return Elasticsearch(hosts={
            self.ServerIp: self.ServerPort
        })

    def get_probability(self,
                        urbanization,
                        terrain_type,
                        close_to_water,
                        poke_stop_distance,
                        gym_distance,
                        continent,
                        appeared_day_of_week,
                        appeared_time_of_day,
                        temperature,
                        pressure,
                        wind_speed,
                        weather_icon
                        ):
        query = {
            "query": {
                "match_all": {

                }
            }
        }
        client = self.connect_to_database()
        res = client.search(
            index="datainput",
            doc_type="json",
            body=query
        )
        for hit in res['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
