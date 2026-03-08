from abc import ABC, abstractmethod
from typing import List
from gameElements.player import Player
from gameElements.agent import Agent
from gameStructure.gameEngine import GameEngine
from gameElements.deck import Deck
from gameElements.team import Team

class GameFactory(ABC):

    GAME_NAME=None

    @classmethod
    @abstractmethod 
    def validate_inital_state(cls, agents: List[Agent], target):
        pass

    @classmethod
    @abstractmethod 
    def create_deck(cls, rules)->Deck:
        pass

    @classmethod
    @abstractmethod
    def create_game(cls, agents: List[Agent], target:int)->GameEngine:
        pass

    @classmethod
    def create_players(cls, agents: List[Agent])->List[Player]:

        player_list=[]

        for i, agent in enumerate(agents):
            player_list.append(Player(i, agent))

        return player_list
    

    @classmethod
    def assign_to_teams(cls, players: List[Player], n_teams: int)->List[Team]:

        teams=[]
        team_size=len(players)//n_teams

        for i in range(n_teams):
            teams.append(Team(str(i),players[team_size*i:team_size*(i+1)]))

        return teams

    


    