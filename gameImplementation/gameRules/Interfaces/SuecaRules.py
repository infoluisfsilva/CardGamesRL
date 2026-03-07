from gameRules import GameRules

class SuecaRules(GameRules):

    def fetch_deck(self, state):
        return super().fetch_deck(state)
    
    def setup(self, state):
        return super().setup(state)