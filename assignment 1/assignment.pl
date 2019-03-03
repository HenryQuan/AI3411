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

% Q2, Same person same name
same_name(P1, P2) :-
    P1 == P2.
% Same Parent and male parent
same_name(C1, C2) :-
    parent(P, C1),
    parent(P, C2),
    male(P).
% father of C
same_name(P, C) :-
    parent(P, C),
    male(P).
same_name(C, P) :-
    parent(P, C),
    male(P).
% grandfather of C
same_name(GP, C) :-
    parent(GP, P),
    male(GP),
    parent(P, C),
    male(P).
same_name(C, GP) :-
    parent(GP, P),
    male(GP),
    parent(P, C),
    male(P).

% Q3, Empty list
sqrt_list([], []).
% One or more elements
sqrt_list([H|T], R) :-
    sqrt_list(T, L),
    R = [[H, S] | L],
    S is sqrt(H).

% Q4, Empty list
sign_runs([], []).
% One element
sign_runs([X], [X]).
% More than one (we need to compare two consecutive)
sign_runs([H, S | T], R) :-
    M > 0,
    M is H * S,
    sign_runs(T, L),
    R = [H, S | L].
sign_runs([H, S | T], R) :-
    M < 0,
    M is H * S,
    sign_runs([S | T], L),
    R = [[H] | L].

% Q5, 