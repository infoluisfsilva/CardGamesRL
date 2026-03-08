from gameStructure.gameEngine import *
from gameImplementation.gameFactories.suecaGameFactory import SuecaGameFactory
from gameImplementation.gameFactories.burroGameFactory import BurroGameFactory
from typing import List
from gameElements.agent import Agent
from gameAgents.forgetfulFreddy  import forgetfulFreddy
from gameAgents.humanHugh  import humanHugh
from gameAgents.savvySally  import savvySally
from gameAgents.randomAgent  import randomAgent

def select_game(game: str, agents: List[Agent], target:int):

    if game == 'sueca':
        engine=SuecaGameFactory.create_game(agents, target)
    #elif game == 'burro':
    #    engine=BurroGameFactory.create_game(agents_types, target)
    else:
        raise ValueError("Unknown game")

    return engine

def main(game, agents, target_score):
    engine=select_game(game, agents, target_score)
    engine.run()

if __name__ == "__main__":

    main('sueca', [forgetfulFreddy(), forgetfulFreddy(), forgetfulFreddy(), forgetfulFreddy()], 3)