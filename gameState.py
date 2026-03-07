class GameState:
    def __init__(self, deck, players, target_score):
        self.deck = deck
        self.players = players
        self.active_players = players
        self.target_score = target_score
        self.current_player_index = 0
        self.round = 0
        self.deck_in_play=[]
        self.history = []
        self.scores = {}
        self.metadata = {}

    @property
    def current_player(self):
        return self.active_players[self.current_player_index]