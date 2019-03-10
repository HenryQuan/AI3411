% concat(List1, List2, Concat_List1_List2):
% Concat_List1_List2 is the concatenation of List1 & List2
concat([], List2, List2).
% OH MY GOD... So you make the head of the first list the head of concat list
% repeat this until you have everything in the concat list and just append list2 (rule 1).
concat([Item | Tail1], List2, [Item | Concat_Tail1_List2]) :-
    concat(Tail1, List2, Concat_Tail1_List2).
