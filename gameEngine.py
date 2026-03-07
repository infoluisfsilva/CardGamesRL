from gameState import *
from gameRules import *
from player import Player

class GameEngine:

    def __init__(self, rules: GameRules, state:GameState) -> None:
        self.rules=rules
        self.state=state

    def run(self):
        self.rules.setup(self.state)
        while not self.rules.is_game_over(self.state):
            self.play_round()

    def play_round(self):
        print(f"Playing round {self.state.round}")
        self.rules.start_round(self.state)

        while not self.rules.is_round_over(self.state):
            self.play_turn()

        self.rules.evaluate_round(self.state)

    def play_turn(self):
        print(f"\tPlayer to play: {self.state.current_player}")
        self.rules.start_turn(self.state)
        player=self.state.current_player

        while not self.rules.is_turn_over(self.state):
            valid_actions=self.rules.valid_actions(player, self.state)
            action = player.choose_action(self.state, valid_actions)
            self.rules.apply_action(self.state, player, action)

        self.rules.evaluate_turn(self.state)