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

% Q2, 

% Q3, 

% Q4,

% Q5, 