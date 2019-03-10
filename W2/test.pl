test(f(A, B, C), D) :-
    A = B, C = D.

% test(f(1, 1, 2), 2). true.
    
% test(f(1, 2, 3), 3). false.
    
% test(f(1, 1, 2), 3). false.
    
% test(f(1, X, 2), 2). X = 1.
    
% test(f(1, _, _), 2). true.
    
% test(f(1, X, 2), Y). X = 1, Y = 2.
    
% test(g(1, X, 2), Y). false.

% test(f(X, 1, Y, 1), 1). X = 1, Y = 1.
% It is false. You got this wrong. I think it is because this f() is not defined.

% test(f(X, 1, Y, 1)). false.

% test(f(X, Y, Z), A). X = Y, Z = A.

% test(f(X, Y), A). false.
    
% test(X, a). X = f(xx, xx, a);