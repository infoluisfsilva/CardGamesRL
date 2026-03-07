from abc import ABC, abstractmethod
from pyswip import Prolog, Atom, Variable
import random
from typing import List, Any, Dict
import ast
from operator import itemgetter

class Game(ABC):

    def play(self):
        self.setup_game()
        self.play_game()

    @abstractmethod
    def play_game(self):
        pass

    @abstractmethod
    def setup_game(self):
        pass

    @property
    @abstractmethod
    def deck(self) -> List[Any]:
        pass

    @property
    @abstractmethod
    def players(self) -> Dict:
        pass

    def _shuffle(self) -> List[Any]:
        shuffled_deck=self.deck.copy()
        random.shuffle(shuffled_deck)
        return shuffled_deck

    def extract_players_info(self, players_query) -> Dict:

        players={}

        for player_str in players_query:
            player_info=player_str[7:-1].split(',')

            players[int(player_info[0])]=Player(int(player_info[0]), int(player_info[1]), ast.literal_eval(player_info[2]), ast.literal_eval(player_info[3]))

        return players
    
    @abstractmethod
    def count_score(self): 
        pass

    @abstractmethod 
    def deal(self, shuffled_deck):
        pass

#class Burro(Game):
#    def __init__(self, prolog, target_points):
#        self.prolog=prolog
#        self.target_points=target_points
#        self.round=0
#        self.history=None
#
#    @property
#    def deck(self):
#        return self._deck
#
#    def setup_game(self):
#        self._deck=list(self.prolog.query("burro:generate_deck(Deck)"))[0]['Deck']
#        #UPDATE CREATE PLAYER LIST PARA BURRO, NÃO TEM DE SER 4
#        self.composition=self.extract_players_info(list(self.prolog.query("burro:create_players(0, PlayerList)"))[0]['PlayerList'])
#        self.round=1
#        
#        print(self.composition)
#
#        self.play_round()
#
#    def play_round(self):
#        shuffled_deck=self._shuffle()
#        print(shuffled_deck)

class Sueca(Game):
    def __init__(self, prolog, target_points):
        self.prolog=prolog
        self.target_points=target_points
        self.round=0
        self.history={}
        self.scores={}
        self.dealing_choices=["top", "bottom"]

    @property
    def deck(self):
        return self._deck
    
    @property
    def players(self)->Dict:
        return self._players
    
    def count_score(self):
        for round, round_info in self.history.items():
            self.scores[round_info['WinningTeam']] = self.scores.get(round_info['WinningTeam'], 0) + round_info['Points']


    def setup_game(self):
        self._deck=list(self.prolog.query("sueca:generate_deck(Deck)"))[0]['Deck']
        self._players=self.extract_players_info(list(self.prolog.query("sueca:create_players(0, PlayerList)"))[0]['PlayerList'])

        print(self._players)

    def reverse_deck(self, deck_to_reverse):
        return deck_to_reverse[::-1]
    
    def call_next(self, first_call, n_calls, direction:int):

        calls=0
         
        while abs(calls)<n_calls:
            player_to_call=(first_call+calls)%len(self.players)
            yield player_to_call
            calls+=direction

    ##Relocate this logic back into sueca.pl - Keep all game logic contained in one place
    def deal(self, shuffled_deck, dealer=1, pos=None):

        deck_to_deal=shuffled_deck.copy()
        inc=1
     
        if pos=='bottom':
            deck_to_deal=self.reverse_deck(deck_to_deal)
            inc=-1

        trump=deck_to_deal[0]

        for player_to_deal_to in self.call_next(dealer, len(self.players), inc):
            self.players[player_to_deal_to].hand=deck_to_deal[:10]
            deck_to_deal=deck_to_deal[10:]

        return trump
    
    def process_pile(self, pile):
        ##check who won ############ prolog
        pile_winner=1

        pile_winner=max(pile, key=itemgetter(1))

        ###add pile to history


        return pile_winner
    

    def play_game(self):
        while all(score<self.target_points for score in self.scores):
            #play round
            self.play_round()

            #update scores

    def play_round(self):
        self.round+=1

        #shuffle deck
        shuffled_deck=self._shuffle()

        #deal
        dealer= self.round%len(self._players)

        #choose top or botom
        pos=random.choice(self.dealing_choices)

        trump=self.deal(shuffled_deck, dealer, pos)

        #print(shuffled_deck, pos, trump)
        print(trump)

        #play piles untill end of round - players with empty hands
        ##check hands of equal sizes and != []
        hands=[player.hand for player in self.players.values()]

        pile_starter=(self.round+1)%len(self.players)
        pile=[]

        #play all 1o hands in round
        while all(hand != [] for hand in hands):                

            for player_to_play in self.call_next(pile_starter, len(self.players), 1):
                pile.append(self.players[player_to_play].play_card())

            #find pile winner and add pile to history
            pile_starter = self.process_pile(pile)

        #check who won round and update scores



class Player:
    def __init__(self, id:int, team:int, hand:List, beliefs:List) -> None:
        self._id=id
        self._team=team
        self._hand=hand
        self._beliefs=beliefs

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

    def play_card(self):
        print(f"{self.id} playing card")
        pass

    def __str__(self):
        return f'Player[id:{self.id}, team:{self.team}, hand:{self.hand}, beliefs: {self.beliefs}]'
    
    def __repr__(self):
        return self.__str__()
    

def game_factory(database:Prolog, game: str, rounds:int)->Game:

    if game=='sueca':
        return Sueca(database, rounds)

    #elif game=='burro':
    #    return Burro(database, rounds)
    
    else:
        raise TypeError

def main(database, game, rounds):
    game=game_factory(database, game, rounds)
    game.play()

if __name__ == "__main__":

    prolog = Prolog()

    prolog.consult("sueca.pl")
    prolog.consult("burro.pl")

    main(prolog, 'sueca', 3)
