from abc import ABC, abstractmethod
from typing import List, Any, Dict
from player import *
from gameEngine import GameEngine
from pyswip import Prolog

class GameFactory(ABC):

    def __init__(self):
        self.database = Prolog()

    def create_players(self, n_players)->List[Player]:
        return [Player(i) for i in range(n_players)]

    @abstractmethod
    def create_game(self, n_players:int, target:int)->GameEngine:
        pass

    @abstractmethod 
    def create_deck(self, n_players)->List:
        pass