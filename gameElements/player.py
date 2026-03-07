from typing import List, Any, Dict
from gameElements.agent import Agent

class Player:
    def __init__(self, id:int, agent:Agent) -> None:
        self._id=id
        self.agent=agent
        self._beliefs=None

    @property
    def id(self):
        return self._id
    
    @property
    def beliefs(self):
        return self._beliefs
    
    @beliefs.setter
    def beliefs(self, new_beliefs):
        self._beliefs=new_beliefs

    def choose_action(self, state, valid_actions):
        print(f"{self.id} playing card")
        pass

    def __str__(self):
        return f'Player[id:{self.id}, beliefs: {self.beliefs}]'
    
    def __repr__(self):
        return self.__str__()