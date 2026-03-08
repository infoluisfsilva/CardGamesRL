from gameElements.agent import Agent
from gameImplementation.gameEnums.gameType import GameType

class forgetfulFreddy(Agent):

    def __init__(self) -> None:
        self.forgetfulnes=0.5

    @property
    def supported_games(self):
        return {GameType.SUECA}
    
    def choose_action(self, player, state, valid_actions):
        return super().choose_action(player, state, valid_actions)