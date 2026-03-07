from gameStructure.gameEngine import *
from gameImplementation.gameFactories.suecaGameFactory import SuecaGameFactory
from gameImplementation.gameFactories.burroGameFactory import BurroGameFactory
from typing import List

def select_game(game: str, agents_types: List[str], target:int):

    if game == 'sueca':
        engine=SuecaGameFactory().create_game(agents_types, target)
    #elif game == 'burro':
    #    engine=BurroGameFactory().create_game(agents_types, target)
    else:
        raise ValueError("Unknown game")

    return engine

def main(game, players, target_score):
    engine=select_game(game, players, target_score)
    engine.run()

if __name__ == "__main__":

    main('sueca', 4, 3)
