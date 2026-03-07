from gameElements.tunrOrder import TurnOrder

class GameState:

    def __init__(self, deck, players, teams=None, target_score=1):
        self.deck = deck
        self.players=players
        self.teams=teams
        self.turn_order=TurnOrder(players)
        self.target_score = target_score
        self.round = 0
        self.deck_in_play=[]
        self.history = []
        self.scores = {}
        self.metadata = {}