/*
    This is the first assignment of COMP3411 T1
    Yiheng Quan Z5098268
*/

% Q1, Handle nothing or one element
sumsq_even([], 0).
% Loop through the list and sum the square of even numbers
sumsq_even([H|T], EvenSum) :-
    sumsq_even(T, Sum),
    0 is H mod 2,
    EvenSum is H * H + Sum.
sumsq_even([H|T], Sum) :-
    sumsq_even(T, Sum),
    1 is H mod 2.

% P1 is an ancestor of P2
ancestor(P1, P2) :-
    parent(P1, P2).
ancestor(P1, P2) :-
    parent(P1, Child),
    ancestor(Child, P2).

% Q2, Same person same name
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

% Q3, Empty list
sqrt_list([], []).
% One or more elements
sqrt_list([H|T], R) :-
    % negative sqrt is not valid
    H > 0,
    sqrt_list(T, L),
    R = [[H , S] | L],
    S is sqrt(H).

% Q4, Empty list
sign_runs([], []).
% One element
sign_runs([X], [X]).
% All you need to know is when to split (when signs are different)
sign_runs([F, S | T], R) :-
    M is F * S,
    M > 0,
    sign_runs(T, L),
    R is [[F | S] | L].

% Q5, Binary Tree
empty().
tree(L, Num, R).