from abc import ABC, abstractmethod

class Agent(ABC):

    @abstractmethod
    def choose_action(self, player, state, valid_actions):
        pass