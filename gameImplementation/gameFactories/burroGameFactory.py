from BurroRules import *
from gameState import *
from gameEngine import *
from gameStructure.gameFactory import GameFactory

class BurroGameFactory(GameFactory):

    def create_game(self, n_players: int, target:int)->GameEngine:

    #   =================Validate initial state==========================
        #validate number of players constraint
        if n_players >=3:
            raise ValueError("Burro requires at least 3 players")
        
        #validate that target is int>0
        if isinstance(target, int) and target > 0:
            raise ValueError("target must be a positive integer")
        
    #   ==================Create game if everything is valid==============
        #connection to prolog db
        self.database.consult('burro.pl')
        
        #create players
        players=self.create_players(n_players)
       
        #set state 
        state = GameState(players, target)

        #connect to interface between rules (prolog) and engine
        rules = BurroRules(self.database)

        return GameEngine(rules, state)