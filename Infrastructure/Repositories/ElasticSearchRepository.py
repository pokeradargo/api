from elasticsearch import Elasticsearch


class ElasticSearchRepository:
    _ServerIp = "pokeradar-elastic-master-dev.sandbox"
    _ServerPort = 9200

    def connect_to_database(self):
        return Elasticsearch(hosts={
            self._ServerIp: self._ServerPort
        })

    def get_probability(self,
                        urbanization,
                        terrain_type,
                        close_to_water,
                        appeared_time_of_day,
                        pokestop,
                        gym,
                        continent,
                        temperature,
                        pressure,
                        wind_speed,
                        weather_icon
                        ):
        query = {
            'query': {
                'bool': {
                    'must': [
                        {'match': {'urbanization': urbanization}},
                        {'match': {'terraintype': terrain_type}},
                        {'match': {'closetowater': close_to_water}},
                        {'match': {'appearedtimeofday': appeared_time_of_day}},
                        {'match': {'pokestopdistance': pokestop}},
                        {'match': {'gymdistance': gym}},
                        {'match': {'continent': continent}},
                        {'match': {'temperature': temperature}},
                        {'match': {'pressure': pressure}},
                        {'match': {'windspeed': wind_speed}},
                        {'match': {'weathericon': weather_icon}}
                    ]
                }
            }
        }

        client = self.connect_to_database()
        res = client.search(
            index="dataoutput",
            doc_type="json",
            body=query
        )
        response = {}
        for hit in res['hits']['hits']:
            response['pokemons'] = hit['_source']['predictedpokemons']
            response['accumulatedprediction'] = hit['_source']['accumulatedprediction']
            break

        return response
