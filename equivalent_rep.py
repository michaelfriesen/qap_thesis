## Computes equivalent problems from
## Representations of quadratic combinatorial optimization problems
## A case study using the quadratic set covering problem
## Punnen and Pandey

import numpy as np

def elimination_colrow(Q,c,n):    # Creates equivalent problem by zeroing last row/column of Q_(i,j)
    for i in range(n):
        for j in range(n):
            c[i, j] += sum(Q[i * n + j, (k * n) - 1] for k in range(1, n)) + sum(Q[i * n + j, (n - 1) * n:n ** 2 - 1])

    for i in range(n - 1):
        for j in range(n):
            Q[:, i * n + j] -= Q[:, ((i + 1) * n) - 1]
    for i in range(n - 1):
        for j in range(n):
            Q[:, (j * n + i)] -= Q[:, (n * (n - 1)) + i]
    return Q,c

## The following choices for U,Y are outlined in section 2 in text above

def dia_elim(Q_dia,c_dia,n):
    c_dia = c_dia + np.diag(Q_dia).reshape((n, n))
    Q_dia = Q_dia - np.diag(np.diag(Q_dia))
    # np.fill_diagonal(Q,0)
    return Q_dia,c_dia

def lin_elim(Q_lin,c_lin,n):
    Q_lin = Q_lin + np.diag(c_lin.reshape(n**2))
    c_lin = c_lin - c_lin
    return Q_lin,c_lin

def symmetry(Q_sym,c_sym):
    Q_sym = 0.5*(Q_sym + np.transpose(Q_sym))
    return Q_sym,c_sym

def positive(Q_pos,c_pos,n):
    M = 10000
    Q_pos = Q_pos + np.diag(M*np.ones(n**2))
    c_pos = c_pos - M*np.ones((n,n))
    return Q_pos,c_pos

def negative(Q_neg,c_neg,n):
    M = 10000
    Q_neg = Q_neg - np.diag(M * np.ones(n ** 2))
    c_neg = c_neg + M*np.ones((n,n))
    return Q_neg, c_neg

def triangular(Q_tri,c_tri,n):
    c_tri = c_tri + np.diag(Q_tri).reshape((n, n))
    Q_tri = np.triu(Q_tri + Q_tri.transpose() - 2 * np.diag(np.diag(Q_tri)))
    return Q_tri,c_tri