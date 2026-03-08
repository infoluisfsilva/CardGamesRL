from typing import List
from gameImplementation.gameRules.Interfaces.SuecaRules import *
from gameImplementation.gameEnums.gameType import GameType
from gameStructure.gameState import *
from gameStructure.gameEngine import *
from gameStructure.gameFactory import GameFactory
from gameElements.player import Player
from gameElements.team import Team
from gameElements.agent import Agent
from gameElements.deck import Deck

class SuecaGameFactory(GameFactory):

    GAME_NAME=GameType.SUECA

    @classmethod
    def validate_inital_state(cls, agents: List[Agent], target):
        #validate number of players constraint
        if len(agents) != 4:
            raise ValueError("Sueca requires 4 players")
        
        #validate that target is int>0
        if not (isinstance(target, int) and target > 0):
            raise ValueError("Target must be a positive integer")
        
        if not all(cls.GAME_NAME in agent.supported_games for agent in agents):
            raise ValueError(f"At least one of the Chosen agents is not suited to play the game of {cls.GAME_NAME}")
    
    @classmethod
    def create_deck(cls, rules: SuecaRules) -> Deck:

        game_deck= []
 
        #Calc number of decks needed from number of players (e.g to play Burro with 9 people you need 2 decks)
        #(for sueca you only ever need 1)
        decks_needed=1

        #Create all decks needed and collapse into one 
        for i in range(decks_needed):
            game_deck.extend(rules.create_deck())

        #later on it is needed to convert this into deck
        return game_deck

    @classmethod
    def create_game(cls, agents: List[Agent], target:int)->GameEngine:

        #   =================Validate initial state==========================
        cls.validate_inital_state(agents, target)
        
    #   ==================Create game if everything is valid==============
        #connect to interface between rules (prolog) and engine
        rules = SuecaRules()
        
        #create players
        players=cls.create_players(agents)

        #assign to teams - Sueca always has 2 teams and earlier we checked that it has the correct number of players
        teams=cls.assign_to_teams(players, 2)

        #create deck
        deck=cls.create_deck(rules)
       
        #set state 
        state = GameState(deck=deck, players=players, teams=teams, target_score=target)

        return GameEngine(rules, state)