from pokemon_sql_db_connection import *
from pokemonNames.pokemonNames import *
import random

class Player:
    def __init__(self, name='Ash Ketchum', city='Pallet Town'):
        self.name = name
        self.city = city
        self.pokemon_caught_list = []

    def search_for_pokemon(self, poke_instance):
        # poke_instance = PokemonNames()
        # pokemon = poke_instance.get_random_name()
        #self.pokemon_encounter = pokemon
        print(f'\n{self.name} brushes through the dense foliage of the forest...')
        print(f'\nA {poke_instance.pokemon_name} appeared!')

    def try_catch_pokemon(self, poke_instance):
        while True:
            print(f'\n{self.name}: "Poke-ball, go!"')
            print(f'\n{poke_instance.pokemon_name} is warped into the pokeball...')

            catch_rate = random.randint(0, 1)
            if catch_rate == 1:
                print(f"\nYou captured a {poke_instance.pokemon_name}!, congrats!")
                print(f"\nSaving {poke_instance.pokemon_name}'s data to pokedex and adding to your inventory...")
                self.pokemon_caught_list.append(poke_instance.pokemon_name)
                joined_list = ','.join(self.pokemon_caught_list)
                break
            else:
                print(f'\n{poke_instance.pokemon_name} burst free out of your pokeball!\n')
                # poke_instance.pokemon_tackle()
                # poke_instance.pokemon_cry()
                # poke_instance.pokemon_rest()

                throw_more = input('\nThrow another? (Y/N): ')
                if throw_more.strip().capitalize() == 'Y':
                    continue
                else:
                    print('You ran away')
                    break

    def save_player_and_pokemon_to_db(self, player_instance):
        #print(self.__pokemon_caught_list)
        #print(joined_list)
        joined_list = ','.join(self.pokemon_caught_list)
        query = (f"INSERT INTO PlayerSave(Name, City, CaughtPokemon) VALUES('{player_instance.name}','{player_instance.city}', '{joined_list}')")
        #print(query)
        cursor.execute(query)
        docker_Pokemon_Game_Db.commit()
        print('\nInventory data successfully saved!')

    def load_player_from_db(self):
        query = 'SELECT * FROM PlayerSave;'
        cursor.execute(query)
        player_results = cursor.fetchall()
        print('\nDisplaying player data:')
        joined_list = ','.join(self.pokemon_caught_list)

        for player in player_results:
            print(player.Name, player.City, player.CaughtPokemon)
            print(Player(player.Name, player.City), player.CaughtPokemon)
            # print(Player(player.Name, player.City), player.CaughtPokemon)
            # new_player = Player(player.Name, player.City, player.CaughtPokemon)
            # print(new_player.name, new_player.city, new_player.pokemon_caught_list)

class Pokemon:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name

    def pokemon_tackle(self):
        print(f'{self.pokemon_name} uses Tackle on you, ouch!')

    def pokemon_cry(self):
        print(f'{self.pokemon_name} makes its poke-noise!')

    def pokemon_rest(self):
        print(f'{self.pokemon_name} eats a poke-snack and takes a nap...')
        print(f'{self.pokemon_name}"s health has been fully restored!')

    def save_pokemon_encounter_to_pokedex_db(self, poke_instance):
        query = (f"INSERT INTO Pokedex(PokemonName) VALUES ('{poke_instance.pokemon_name}')")
        cursor.execute(query)
        docker_Pokemon_Game_Db.commit()
        print('Pokemon encounter successfully updated on pokedex!')

    def load_pokedex_data_from_db(self):
        query = 'SELECT * FROM Pokedex;'
        cursor.execute(query)
        poke_results = cursor.fetchall()
        print('Loading Pokedex data...')

        for pokemon in poke_results:
            load_poke = Pokemon(pokemon.PokemonName)
            print(load_poke.pokemon_name)
        print('\nPokedex data successfully loaded.')


# __name__/__main__ for pokemon game:
print("Pokemon game OOP class file:", __name__)

if __name__ == '__main__':
    print("Running game directly through main file")
else:
    print('Running game through executable.')