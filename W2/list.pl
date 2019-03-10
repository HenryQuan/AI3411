is_a_list([]).
is_a_list(.(_, Tail)) :-
    is_a_list(Tail).

% is_a_list([]). true.
    
% is_a_list(.(a, [])). true.
    
% is_a_list(.(a, b)). false.
    
% is_a_list(a). false.

head_tail([H | T], Head, Tail) :-
    Head = H,
    Tail = T.

% base case
is_member(Element, list(Element, _)).

% recursive case (to be completed!)
is_member(Element, list(_, Tail)) :-
    is_member(Element, Tail).

% is_member(X, list(1, list(2, list(3, nil)))).
% X will be 1, 2 or 3 to be a member of list(1, 2, 3).

% [1, 2, 3, 4, 5, 6] = [Head | Tail].
% Head = 1, Tail = [2, 3, 4, 5, 6].
	
% [1, 2] = [Head | Tail].
% Head = 1, Tail = [2].

% [1] = [Head | Tail].
% Head = 1, Tail = ??. Tail = [] (It is empty)
	
% [] = [Head | Tail].
% false (It seems that Head cannot be null)
	
% [Head | Tail] = [[1, 2], [3, 4, [5, 6]], [7, 8], 9].
% Head = [1, 2], Tail = [[3, 4, [5, 6]], [7, 8], 9].
	
% What = [a | [b, c, d]].
% What = [a, b, c, d]. (combined all of them?)
	
% What = [a | [b]].
% What = [a, b].
	
% What = [[a] | [b]].
% What = [[a], b]. (be careful it is [a])
	
% What = [a | b].
% What = [a, b]. It is What = [a|b] ??? what?

% In what way do the predicates member and is_member behave differently?
% member outputs [] but is_member outputs list(list(...))

cons([], L, L).
cons([H1 | T1], L2, [H1 | Rest]) :-
    cons(T1, L2, Rest).