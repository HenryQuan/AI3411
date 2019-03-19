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

% append new item to list
my_append([], N, [[N]]).
my_append([H | T], N, [H | R]) :-
    my_append(T, N, R).

% Empty list
sign_runs([], []).
% one item
sign_runs([X], [[X]]).
sign_runs([X, []], [[X]]).
sign_runs([[], X], [[X]]).
% Positive
sign_runs([F, S | T], [[F | R]]) :-
    F >= 0, S >= 0,
    sign_runs([S | T], [R]).
sign_runs([F, S | T], [[F | R]]) :-
    F < 0, S < 0,
    sign_runs([S | T], [R]).
% Negative
sign_runs([F, S | T], [[F] | R]) :-
    F >= 0, S < 0,
    sign_runs([S | T], R).
sign_runs([F, S | T], [[F] | R]) :-
    F < 0, S >= 0,
    sign_runs([S | T], R).

% --- Q5 ---

% Binary Tree
empty().
tree(L, Num, R).
