from abc import ABC, abstractmethod

class GameRules(ABC):

    @abstractmethod
    def fetch_deck(self, state): pass

    @abstractmethod
    def setup(self, state): pass

    @abstractmethod
    def start_round(self, state): pass

    @abstractmethod
    def is_round_over(self, state): pass

    @abstractmethod
    def start_turn(self, state): pass

    @abstractmethod
    def is_turn_over(self, state): pass

    @abstractmethod
    def is_game_over(self, state): pass

    @abstractmethod
    def valid_actions(self, state, player): pass

    @abstractmethod
    def apply_action(self, state, player, action): pass

    @abstractmethod
    def evaluate_round(self, state): pass

    @abstractmethod
    def evaluate_turn(self, state): pass

