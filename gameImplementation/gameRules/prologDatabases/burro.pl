:- module(burro, [generate_deck/1]).
:- use_module(library(random)).


%%%%%%%%%%%%GENERAL COMPOSITION FOR A DECK%%%%%%%%
%4 SUITS
suit(hearts).
suit(diamonds).
suit(clubs).
suit(spades).

%CARDS ACE THORUGH KING
value(ace).
value(2).
value(3).
value(4).
value(5).
value(6).
value(7).
value(8).
value(9).
value(10).
value(jack).
value(queen).
value(king).


%%%%CREATE CARD SPECIFICATIONS SUITED FOR SPECIFIC GAME%%%%%%%%%%%%%5

%IN SUECA YOU DONT USE 8,9,10. NUMBERED CARDS (EXCEPT 7) HAVE NO VALUE ETC ETC
value_rank_points_sueca(2, 2, 0).
value_rank_points_sueca(3, 3, 0).
value_rank_points_sueca(4, 4, 0).
value_rank_points_sueca(5, 5, 0).
value_rank_points_sueca(6, 6, 0).
value_rank_points_sueca(7, 10, 10).
value_rank_points_sueca(jack, 8, 3).
value_rank_points_sueca(queen, 7, 2).
value_rank_points_sueca(king, 9, 4).
value_rank_points_sueca(ace, 11, 11).

%IN Burro 
value_rank_points_burro(2, 2, _).
value_rank_points_burro(3, 3, _).
value_rank_points_burro(4, 4, _).
value_rank_points_burro(5, 5, _).
value_rank_points_burro(6, 6, _).
value_rank_points_burro(7, 7, _).
value_rank_points_burro(8, 8, _).
value_rank_points_burro(9, 10, _).
value_rank_points_burro(10, 9, _).
value_rank_points_burro(jack, 10, _).
value_rank_points_burro(queen, 11, _).
value_rank_points_burro(king, 12, _).
value_rank_points_burro(ace, 13, _).

%%%%%%%% GENERATE DECK USING CORRECT SPECS FOR EACH GAME

% card_with_info_*game*(+Suit, +Value, -Card)

%%sueca
card_with_info_sueca(Suit, Value, card(Suit, info(Value, Rank, Points))) :- value_rank_points_sueca(Value, Rank, Points).

generate_deck_sueca(Deck) :-
    findall(Card, (
        suit(Suit),
        value(Value),
        card_with_info_sueca(Suit, Value, Card)
    ), Deck).

%%Burro
card_with_info_burro(Suit, Value, card(Suit, info(Value, Rank, Points))) :- value_rank_points_burro(Value, Rank, Points).

generate_deck(Deck) :-
    findall(Card, (
        suit(Suit),
        value(Value),
        card_with_info_burro(Suit, Value, Card)
    ), Deck).

%%%%%%%%%%%SHUFFLE
choose(Deck, Card) :- length(Deck, Len), Bound is Len, random(0, Bound, Index), nth0(Index, Deck, Card).

shuffle([], []).
shuffle(Deck, [Elt|L3]) :- choose(Deck, Elt), select(Elt, Deck, RemainingDeck), shuffle(RemainingDeck, L3).

%%%%%%%%%%create PlayerList

create_players_sueca(I, [Player|RemainingPlayers]):- 4>I, !, IncI is I+1, Team is I mod 2, Player = player(I, Team, [],[]), create_players_sueca(IncI, RemainingPlayers). 
create_players_sueca(_, _).

%%%%%%%%%%%next player (implemented by mod)

%%%%Play Card
play_card(player(_,_,Hand,_), Pile):- choose(Hand, Card), select(Card, Hand).

%%%Play Pile
%%%%%%%%%%%PLAY Round
play_round(Deck, PlayerList, Round, [History|Future]):-play_pile(PlayerList).

%%%%%%%Count Points
count_points().

%%%%COUNT ROUND WINS UPDATE
%count_round_wins(+Team, +History, -Count) - count Team victories recorded in History
count_round_wins(Team, [], 0).
count_round_wins(Team, [Team|Tail], Count) :- Count is BaseCount+1, count_points(Team, Tail, BaseCount).
count_round_wins(Team, [H|Tail], Count) :- dif(Team, H), count_points(Team, Tail, Count).


%%%%%%%%%%Play game

game_sueca(Deck, PlayerList, TargetPoints, Round, [History|Future]) :- count_points(0, History, T1Points), count_points(1, History, T2Points), TargetPoints>T1Points, TargetPoints>T2Points, !, play_round().

%%%%%%%%%%%%%%%%%%CHOOSE TRUMP

%choose_trump_sueca(Player, Deck, Pos, Card, Suit):-

%%%%%%%%%%%%%%DEAL
%deal_sueca(_,_,[]).
%deal_sueca(Player, PlayerList, Pos, [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10 | RemainingDeck]):-
%deal_sueca(Player, PlayerList, Pos, Deck):- 

%%%%%%%%%%%%%%%%SEARCH DECK (THIS IS A TESTER, OBJECTIVE IN THE FUTURE WILL BE TO SEARCH HAND or LIST OF UNPLAYED CARDS NOT ON PLAYER HANDS) FOR SUITED
filter_suit(Suit, Deck, Filtered) :- findall(card(Suit, info(V, R, P)), (member(card(Suit, info(V, R, P)), Deck)), Filtered).


