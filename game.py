from gameEngine import *
from suecaGameFactory import SuecaGameFactory
from burroGameFactory import BurroGameFactory

def select_game(game: str, n_players: int, target:int):

    if game == 'sueca':
        engine=SuecaGameFactory().create_game(n_players, target)
    elif game == 'burro':
        engine=BurroGameFactory().create_game(n_players, target)
    else:
        raise ValueError("Unknown game")

    return engine

def main(game, players, target_score):
    engine=select_game(game, players, target_score)
    engine.run()

if __name__ == "__main__":

    main('sueca', 4, 3)
