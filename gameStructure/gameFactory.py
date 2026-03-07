from abc import ABC, abstractmethod
from typing import List, Any, Dict
from gameElements.player import *
from gameStructure.gameEngine import GameEngine
from gameElements.deck import Deck
from pyswip import Prolog

class GameFactory(ABC):

    def __init__(self):
        self.database = Prolog()

    @abstractmethod 
    def validate_inital_state(self, agents_types: List[str], target):
        pass

    @abstractmethod
    def create_players(self, agents_types: List[str])->List[Player]:
        pass
    
    @abstractmethod 
    def create_deck(self)->Deck:
        pass

    @abstractmethod
    def create_game(self, agents_types: List[str], target:int)->GameEngine:
        pass

    