% how does this work?
% This is to define what is a descendant
descendant(Person, Descendant) :-
    parent(Person, Descendant).
% This is recursion to find all descendants
descendant(Person, Descendant) :-
    parent(Person, Child),
    descendant(Child, Descendant).