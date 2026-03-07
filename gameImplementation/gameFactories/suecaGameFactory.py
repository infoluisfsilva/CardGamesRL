from typing import List
from gameImplementation.gameRules.Interfaces.SuecaRules import *
from gameStructure.gameState import *
from gameStructure.gameEngine import *
from gameStructure.gameFactory import GameFactory
from gameElements.player import List, Player
from gameElements.deck import Deck

class SuecaGameFactory(GameFactory):

    def __init__(self):
        super().__init__()

        self.valid_agent_list=['humanHugh', ]

    def validate_inital_state(self, agents_types: List[str], target):
        #validate number of players constraint
        if len(agents_types) != 4:
            raise ValueError("Sueca requires 4 players")
        
        #validate that target is int>0
        if isinstance(target, int) and target > 0:
            raise ValueError("Target must be a positive integer")
        
        if not all(agent_type in self.valid_agent_list for agent_type in agents_types):
            raise ValueError("Agent not suited for the game")
        
    def create_players(self, agents_types: List[str]) -> List[Player]:
        return super().create_players(agents_types)
    
    def assign_to_teams(self, players: List[Player]):
        pass
    
    def create_deck(self) -> Deck:
        pass

    def create_game(self, agents_types: List[str], target:int)->GameEngine:

        #   =================Validate initial state==========================
        self.validate_inital_state(agents_types, target)
        
    #   ==================Create game if everything is valid==============
        #connection to prolog db
        self.database.consult('sueca.pl')

        #connect to interface between rules (prolog) and engine
        rules = SuecaRules(self.database)
        
        #create players
        players=self.create_players(agents_types)

        #assign to teams
        teams=self.assign_to_teams(players)

        #create deck
        deck=self.create_deck()
       
        #set state 
        state = GameState(deck=deck, players=players, teams=teams, target_score=target)

        return GameEngine(rules, state)