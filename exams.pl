
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%IMPORTING PREVIOUS FUNCTIONS IMPLEMENTED%%%%%%%%%%%%%%%%%%%%%%%%%

%range(X,X,[]) if you want range to behave like in python where the end is exclusive
range(X,X,[X]).
range(Start, Stop, [Start|Solution]):-Start<Stop, NewStart is Start +1, range(NewStart, Stop, Solution).

%remove first occurrence
remove(X, [X|Tail], Tail).
remove(X, [Head|Tail], [Head|Tail1]):-remove(X,Tail,Tail1).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%PATH IN A GRAPH%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
graph_path(G, N1, N2, Path):-graph(G), check_path(G,N1,N2, Path).

graph([]):-!.
graph([Head|Tail]):-length(Head,L), L is 2, graph(Tail).

check_path(_,N, N, [N]):-!.
check_path(G,N1,N2, [N1|Path]):- select([N1,N3], G, G1), check_path(G1,N3,N2, Path).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Count appearences of each element in lsit%%%%%%%%%%%%%%%%%%
instances(L):-count_instances(L, [], Result), write(Result).

count_instances([], I, I):-!.
count_instances([Value|Tail], I, Result):- select([Value,Count], I, I1), !, NewCount is Count+1, append([[Value, NewCount]], I1, NewI),
                                            count_instances(Tail, NewI, Result).  %increment count
count_instances([Value|Tail], I, Result):- append([[Value,1]], I, NewI), count_instances(Tail, NewI, Result). %add element

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%DOMINO PROBLEM%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%test_chain([[D1,D2]|T]):- chain([[D1,D2]|T], R1); chain([[D2,D1]|T], R2), write(R1), write(R2).

chain([],[]):-!.
chain([[D1,D2]],[[D1,D2]]):-!.
%chain([[D1,D2], [D3,D4]|Tail], R):-D1 is D3; D1 is D4, chain([[D2,D1],[D3,D4]|Tail],R). %Trying to add rotation on the first piece  
chain([[D1,D2], [D3,D4]|Tail], [[D1,D2]|R]):-D2 is D3, chain([[D3,D4]|Tail],R). %the domino is in the correct position. 
chain([[D1,D2], [D3,D4]|Tail], [[D1,D2]|R]):-D2 is D4, chain([[D4,D3]|Tail],R). %the domino is reversed

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%TUTORIAL DOMINO PROBLEM%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
chains([],[]).
chains([[X,Y]], [[X,Y]]).
chains([[X,Y]], [[Y,X]]).
chains([[X,Y]|L], [[X,Y]|R]) :- chains(L,R), R = [ [Y,_] | _ ].
chains([[X,Y]|L], [[Y,X]|R]) :- chains(L,R), R = [ [X,_] | _ ].

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%ADVANCED ROOT%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nth_root(N,K,R):-range(0,K,L), member(R,L), K>=R**N, R1 is R+1,K<R1**N.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%ALL SUBSEQUENCES THAT ADD UP TO A PERFECT SQUARE%%%%%%%%%%%%%%%%%%%%%%%%
allSSSS(L):-append(_,Tail,L), append(SS,_,Tail), pss(SS, Sum), write(Sum-SS), nl, fail.
allSSSS(_).

pss(L,Sum):-sum_list(L,Sum), Sum>0, range(0,Sum,Range), member(R,Range),Sum is R*R.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%RIVER CROSSING%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%My first attempt. Close but no cigar, I do not keep a record of the steps taken to avoid repetition. Endless cycles
%river_crossing(LBM,LBC,RBM,RBC, Crossing):- cross(LBM, LBC, RBM ,RBC, CM, CC, LBM1, LBC1, RBM1, RBC1,Crossing),Crossing1 is Crossing+1, river_crossing(LBM1, LBC1, RBM1, RBC1, Crossing1).
%
%cross(LBM, LBC, RBM ,RBC, CM, CC, LBM1, LBC1, RBM1, RBC1, Crossing):- even(Crossing),!,range(0,LBM,AM), member(CM, AM), range(0,LBC,AC), member(CC, AC), CC+CM =< 2, change_banks(RBM, RBC, LBM, LBC, CM, CC, RBM1, RBC1, LBM1, LBC1), check_state(LBM1, LBC1, RBM1, RBC1).
%cross(LBM, LBC, RBM ,RBC, CM, CC, LBM1, LBC1, RBM1, RBC1, _):-range(0,RBM,AM), member(CM, AM), range(0,RBC,AC), member(CC, AC), CC+CM =< 2, change_banks(LBM, LBC, RBM, RBC, CM, CC, LBM1, LBC1, RBM1, RBC1), check_state(LBM1, LBC1, RBM1, RBC1).
%
%even(N):- mod(N,2) =:= 0.
%change_banks(BM_add, BC_add, BM_remove, BC_remove, CM, CC, BM_add1, BC_add1, BM_remove1, BC_remove1):- BM_add1 is BM_add+CM, BC_add1 is BC_add+CC, BM_remove1 is BM_remove-CM, BC_remove1 is BC_remove-CC.
%check_state(LBM, LBC, RBM ,RBC):-LBM>=LBC, RBM>=RBC.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%MY SOLUTION - STRIPS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%river_crossing(Plan):-solve([at(canoe, left_bank), space(canoe), space(canoe), at(missionary1, left_bank), at(missionary2, left_bank), at(missionary3, left_bank), at(cannibal1, left_bank), at(cannibal2, left_bank), at(cannibal3, left_bank)], 
%                            [at(missionary1, right_bank), at(missionary2, right_bank), at(missionary3, right_bank), at(cannibal1, right_bank), at(cannibal2, right_bank), at(cannibal3, right_bank)], 
%                            [], Plan).

river_crossing(Plan):-solve([at(canoe, left_bank), space(canoe), space(canoe), at(missionary, left_bank), at(missionary, left_bank), at(missionary, left_bank), at(cannibal, left_bank), at(cannibal, left_bank), at(cannibal, left_bank)], 
                            [at(missionary, right_bank), at(missionary, right_bank), at(missionary, right_bank), at(cannibal, right_bank), at(cannibal, right_bank), at(cannibal, right_bank)], 
                            [], Plan).                        

%solve(InitialState, FinalState, PartialPlan, Plan)
solve(InitialState, FinalState, Plan, Plan):-subset(FinalState, InitialState), !, write(Plan). %check if we have achieved FinalState
solve(InitialState, FinalState, PartialPlan, Plan):-action(A, PC, Del, Add), subset(PC, InitialState), \+member(A,PartialPlan), delete_atoms(Del,InitialState,DelState), append(Add, DelState, NewState), solve(NewState, FinalState, [A|PartialPlan], Plan). %pick an action to perform. Check if preconditions exist in state. Delete atoms that are no longer true. Add new atoms.


action(board(X, Y), [at(canoe, Y), space(canoe), at(X, Y)], [space(canoe), at(X,Y)], [at(X, canoe)]).
action(unboard(X, Y), [at(canoe, Y), at(X, canoe)], [at(X, canoe)], [space(canoe), at(X,Y)]).
action(cross(canoe, right_bank), [at(canoe, left_bank), at(_,canoe)], [at(canoe, left_bank)], [at(canoe, right_bank)]).
action(cross(canoe, left_bank), [at(canoe, right_bank), at(_,canoe)], [at(canoe, right_bank)], [at(canoe, left_bank)]).

delete_atoms([], DelState, DelState):-!. %we have finished deleting atoms from state
delete_atoms([Head|Tail], State, DelState):-remove(Head, State, Aux), delete_atoms(Tail, Aux, DelState).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%TUTORIAL SOLUTION%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
path( E,E, C,C ).
path( ActualState, FinalState, PathSoFar, TotalPath ):-
	oneStep( ActualState, NextState ),
	\+member(NextState,PathSoFar),
	path( NextState, FinalState, [NextState|PathSoFar], TotalPath ).

optimalSolution:-
	between(0,20,N),                         % We look for solution of "cost" 0; if not, of 1, etc.
	path([left,3,3],[right,0,0],[[left,3,3]],C), 
	length(C,N),                   % the cost is the length of C.
	write(C),   % we write the path
	write('\n'), % new line
	write(N).   % we write the cost of the solution
	
	
validState([MissionariesA,CannibalsA]):-	MissionariesA>=0,
	MissionariesA=<3,
	CannibalsA>=0,
	CannibalsA=<3,
	dontEat(MissionariesA,CannibalsA),
	MissionariesB is 3-MissionariesA,
	CannibalsB is 3-CannibalsA,
	dontEat(MissionariesB,CannibalsB).
            
            
% dontEat(M,C) returns true if the cannibals don´t eat the missionaries 

dontEat(0,_).
dontEat(M,C):- M >= C.


% move the difference -2 missionarie from left to right
oneStep([left,M,C],[right,MM,C]):-
    MM is M-2,
    validState([MM,C]).

% move the difference -2 cannibal from left to right
oneStep([left,M,C],[right,M,CC]):-
    CC is C-2,
    validState([M,CC]).

% move the difference +1 missionaries and cannibals
oneStep([left,M,C],[right,MM,CC]):-
    MM is M+1,
    CC is C+1,
    validState([MM,CC]).
    
% move the difference -1 missionarie from left to right    
oneStep([left,M,C],[right,MM,C]):-
    MM is M-1,
    validState([MM,C]).
    
% move the difference -1 cannibal from left to right
oneStep([left,M,C],[right,M,CC]):-
    CC is C-1,
    validState([M,CC]).
    
% move the difference +2 missionarie from right to left
oneStep([right,M,C],[left,MM,C]):-
    MM is M+2,
    validState([MM,C]).
    
% move the difference +2 cannibal from right to left
oneStep([right,M,C],[left,M,CC]):-
    CC is C+2,
    validState([M,CC]).
    

% move the difference +1 missionaries and cannibals
oneStep([right,M,C],[left,MM,CC]):-
    MM is M+1,
    CC is C+1,
    validState([MM,CC]).

% move the difference +1 missionarie from right to left
oneStep([right,M,C],[left,MM,C]):-
    MM is M+1,
    validState([MM,C]).

% move the difference +1 cannibal from right to left
oneStep([right,M,C],[left,M,CC]):-
    CC is C+1,
    validState([M,CC]).

%%%%%%%%%%%%%%%%%%%%%%%
%canoe(m,1).
%canoe(c,2).
%findall(X,canoe(_,X),L), sum_list(L, S).







