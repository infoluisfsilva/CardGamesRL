from pyswip import Prolog
from gameStructure.gameRules import GameRules

class SuecaRules(GameRules):

    def __init__(self) -> None:
        self.database=self.consult_prolog("../gameImplementation/gameRules/prologDatabases/sueca.pl")

    def create_deck(self):
        return list(self.database.query("generate_deck(Deck)"))[0]['Deck']
    
    def setup(self, state):
        return super().setup(state)