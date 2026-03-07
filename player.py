from typing import List, Any, Dict

class Player:
    def __init__(self, id:int) -> None:
        self._id=id
        self._team=None
        self._hand=None
        self._beliefs=None

    @property
    def id(self):
        return self._id
    
    @property
    def team(self):
        return self._team
    
    @property
    def hand(self):
        return self._hand
    
    @hand.setter
    def hand(self, new_hand):
        self._hand=new_hand
    
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
        return f'Player[id:{self.id}, team:{self.team}, hand:{self.hand}, beliefs: {self.beliefs}]'
    
    def __repr__(self):
        return self.__str__()