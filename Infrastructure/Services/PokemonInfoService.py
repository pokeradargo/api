from Infrastructure.Repositories.PostgresqlRepository import PostgresqlRepository


class PokemonInfoService:
    __PokemonRepository = None

    def __init__(self):
        self.__PokemonRepository = PostgresqlRepository()

    def get_pokemon_names(self, pokemon_list):
        pokemon_info = self.__PokemonRepository.get_pokemon_info(pokemon_list)
        pokemon_response = []
        for item in pokemon_info:
            pokemon_response.append(item[1].strip())

        return pokemon_response

