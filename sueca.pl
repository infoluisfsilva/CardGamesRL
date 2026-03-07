:- module(sueca, [generate_deck/1, create_players/2, deal/6]).
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
value_rank_points(2, 2, 0).
value_rank_points(3, 3, 0).
value_rank_points(4, 4, 0).
value_rank_points(5, 5, 0).
value_rank_points(6, 6, 0).
value_rank_points(7, 10, 10).
value_rank_points(jack, 8, 3).
value_rank_points(queen, 7, 2).
value_rank_points(king, 9, 4).
value_rank_points(ace, 11, 11).

%%%%%%%% GENERATE DECK USING CORRECT SPECS FOR EACH GAME

% card_with_info_*game*(+Suit, +Value, -Card)

%%sueca
card_with_info(Suit, Value, card(Suit, info(Value, Rank, Points))) :- value_rank_points(Value, Rank, Points).

generate_deck(Deck) :-
    findall(Card, (
        suit(Suit),
        value(Value),
        card_with_info(Suit, Value, Card)
    ), Deck).

%%%%%%%%%%create PlayerList

create_players(I, [Player|RemainingPlayers]):- 4>I, !, IncI is I+1, Team is I mod 2, Player = player(I, Team, [],[]), create_players(IncI, RemainingPlayers). 
create_players(_, _).


%%%%%%%Count Points
count_points().

%%%%Playable Cards
playable_cards(player(_,_,Hand,_), Pile):- choose(Hand, Card), select(Card, Hand).

%%%%%%%%%%%%Prepare deck for dealing
prepare_deal(Pos, Deck, DeckForDealing):- (Pos == top -> DeckForDealing = Deck;  reverse(Deck, DeckForDealing)).

%%%%%%%%%%%%%%%%%%CHOOSE TRUMP

choose_trump([TrumpCard|_], TrumpCard).

%%%%%%%%%Update who dealer is dealing to
update_recipient(Pos, Dealt, DealingToNext) :-
    ( Pos == top ->
        DealingToNext is (Dealt + 1) mod 4
    ;
        DealingToNext is (Dealt - 1) mod 4
    ).

%%%%%%%%%deal HANDS
%deal_hands(+DealingTo, +DeckForDealing, +Pos, -PlayerToHandCorrespondence)
deal_hands(_,[],_,[]).
deal_hands(DealingTo, [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10 | RemainingDeck], Pos, [[DealingTo, [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10]]|RemainingCorrespondences]):- 
    update_recipient(Pos, DealingTo, DealingToNext), deal_hands(DealingToNext, RemainingDeck, Pos, RemainingCorrespondences).

%%%%%%%%%%%%%%DEAL
deal(Deck, Dealer, Pos, TrumpCard, PlayerToHandCorrespondence):-prepare_deal(Pos, Deck, DeckForDealing), choose_trump(DeckForDealing, TrumpCard), deal_hands(Dealer, DeckForDealing, Pos, PlayerToHandCorrespondence).


%%%%%%%%%%%%%%%%SEARCH DECK (THIS IS A TESTER, OBJECTIVE IN THE FUTURE WILL BE TO SEARCH HAND or LIST OF UNPLAYED CARDS NOT ON PLAYER HANDS) FOR SUITED
filter_suit(Suit, Deck, Filtered) :- findall(card(Suit, info(V, R, P)), (member(card(Suit, info(V, R, P)), Deck)), Filtered).


