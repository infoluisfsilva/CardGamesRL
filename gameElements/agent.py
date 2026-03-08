from abc import ABC, abstractmethod
from gameImplementation.gameEnums.gameType import GameType

class Agent(ABC):

    @property
    @abstractmethod
    def supported_games(self)->set[GameType]:
        pass

    @abstractmethod
    def choose_action(self, player, state, valid_actions):
        pass