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
same_name(N1, N2) :-
    N1 == N2.
% N1 is the parent of N2 or vice versa and a male parent
same_name(N1, N2) :-
    parent(N1, N2),
    male(N1).
same_name(N1, N2) :-
    parent(N2, N1),
    male(N2).
% Same Parent and male parent
same_name(N1, N2) :-
    parent(X, N1),
    parent(X, N2),
    male(X).
% GRANDPARENT???

% Q3, 

% Q4,

% Q5, 