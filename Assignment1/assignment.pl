/*
    This is the first assignment of COMP3411 T1,
    mainly prolog questions.

    Yiheng Quan Z5098268
*/

% --- Q1 ---

% Handle nothing or one element
sumsq_even([], 0).
% Loop through the list and sum the square of even numbers
sumsq_even([H|T], EvenSum) :-
    sumsq_even(T, Sum),
    0 is H mod 2,
    EvenSum is H * H + Sum.
sumsq_even([H|T], Sum) :-
    sumsq_even(T, Sum),
    1 is H mod 2.

% --- Q2 ---

% P1 is an ancestor of P2
ancestor(P1, P2) :-
    parent(P1, P2).
ancestor(P1, P2) :-
    parent(P1, Child),
    ancestor(Child, P2).

% Same person same name
same_name(P, P).
% Same male ancestor
same_name(P1, P2) :-
    ancestor(A, P1),
    ancestor(A, P2),
    male(A).
% Ancestor of C
same_name(P, C) :-
    ancestor(P, C),
    male(P).
same_name(C, P) :-
    ancestor(P, C),
    male(P).

% --- Q3 ---

% Empty list
sqrt_list([], []).
% One or more elements
sqrt_list([H | T], [[H, S] | R]) :-
    % negative sqrt is not valid
    H >= 0, S is sqrt(H),
    sqrt_list(T, R).

% --- Q4 ---

% 20/03/2019 11:04pm solved!

% This question took me around two weeks to solve it.

% Why is it so hard?
% Base cases are not really hard, comparison is not that hard (e.g. [1, -1, 1]. You need to compare 1, -1 and then -1, 1).
% The hard part is how to append and close the bracket.
% 

% shorten my code
same_sign(X, Y) :- X >= 0, Y >= 0.
same_sign(X, Y) :- X < 0, Y < 0.

% Empty list
sign_runs([], []).
% one item
sign_runs([X], [[X]]).
% Same sign
sign_runs([F, S | T], [[F | H] | R]) :-
    same_sign(F, S),
    sign_runs([S | T], [H | R]). % I simply forgot that you can do this -> [H | R]
% Different sign
sign_runs([F, S | T], [[F], H | R]) :-
    not(same_sign(F, S)),
    sign_runs([S | T], [H | R]).

% --- Q5 ---

% no leaves
is_heap(tree(empty, _, empty)).
% check both sides
is_heap(tree(tree(L1, N1, R1), N, tree(L2, N2, R2))) :-
    N1 >= N, N2 >= N,
    is_heap(L1), is_heap(R1), 
    is_heap(L2), is_heap(R2).
% left side
is_heap(tree(tree(L, N, R), M, _)) :-
    N >= M,
    is_heap(L), is_heap(R).
% right side
is_heap(tree(_, M, tree(L, N, R))) :-
    N >= M,
    is_heap(L), is_heap(R).
