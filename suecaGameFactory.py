from typing import List
from SuecaRules import *
from gameState import *
from gameEngine import *
from gameFactory import GameFactory
from player import List, Player

class SuecaGameFactory(GameFactory):

    #overrides method because for Sueca players are divided into teams
    def create_players(self, n_players) -> List[Player]:
        return super().create_players(n_players)
    

    def create_game(self, n_players: int, target:int)->GameEngine:

    #   =================Validate initial state==========================
        #validate number of players constraint
        if n_players != 4:
            raise ValueError("Sueca requires 4 players")
        
        #validate that target is int>0
        if isinstance(target, int) and target > 0:
            raise ValueError("target must be a positive integer")
        
    #   ==================Create game if everything is valid==============
        #connection to prolog db
        self.database.consult('sueca.pl')

        #connect to interface between rules (prolog) and engine
        rules = SuecaRules(self.database)
        
        #create players
        players=self.create_players(n_players)

        #create deck
        deck=
       
        #set state 
        state = GameState(players, target)


        return GameEngine(rules, state)