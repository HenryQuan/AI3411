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
append_new([], N, [N]).
append_new([H | T], N, [H | R]) :-
    append_new(T, N, R).

% append new item to the last item in the list
append_last([], N, [N]).
append_last([L], N, R) :-
    append_new(L, N, R).
append_last([H | T], N, [H | R]) :-
    append_last(T, N, R).

% check if same sign (all positive or all negative)
same_sign(X, Y) :- X >= 0, Y >= 0.
same_sign(X, Y) :- X < 0, Y < 0.

% Empty list
sign_runs([], []).
sign_runs([], F).
% use sign_runs to solve this question
sign_runs(L, R) :- sign_runs(L, R, []).

% flip the list
sign_runs(F, L, []) :-
    flip(L, R), reverse(R, F).

% handle last item, empty result
sign_runs([L], [], [F | T]) :-
    same_sign(L, F),
    sign_runs([], [L, F | T], []).
sign_runs([L], [], [F | T]) :-
    not(same_sign(L, F)),
    sign_runs([], [[L] | [F | T]], []).
% handle last item, some items
sign_runs([L], C, [F | T]) :-
    same_sign(L, F),
    sign_runs([], [[L, F | T] | C], []).
sign_runs([L], C, [F | T]) :-
    not(same_sign(L, F)),
    sign_runs([], [[L], [F | T] | C], []).
% empty result list
sign_runs([F, S | T], [], []) :-
    same_sign(F, S),
    sign_runs([S | T], [], [F]).
sign_runs([F, S | T], [], []) :-
    not(same_sign(F, S)),
    sign_runs([S | T], [F], []).
% empty temp list
sign_runs([F, S | T], C, []) :-
    same_sign(F, S),
    sign_runs([S | T], C, [F]).
sign_runs([F, S | T], C, []) :-
    not(same_sign(F, S)),
    sign_runs([S | T], [[F] | C], []).
% some items
sign_runs([F, S | T], C, R) :-
    same_sign(F, S),
    sign_runs([S | T], C, [F | R]).
sign_runs([F, S | T], C, R) :-
    not(same_sign(F, S)),
    sign_runs([S | T], [[F | R] | C], []).

% --- Q5 ---

% Binary Tree
empty().
tree(L, Num, R).