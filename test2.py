from equivalent_rep import *
from gurobi_model import *
from reading import *
from gurobipy import *

for p in range(1,2):
    for n in range(5,10,5):
        for v in range(0,1):
# for p in range(6,7):
#     for n in range(5,10,5):
#         for v in range(7,8):
            if (n == 10 and v > 4):
                continue
            if (n == 15 and v > 0):
                continue

            # Run original model
            Q,c = read_matrix(n,p,v)
            # Q_sym, c_sym = symmetry(Q, c)
            Q_pos, c_pos = positive(Q, c, n)
            Q_neg, c_neg = negative(Q, c, n)
            Q_tri, c_tri = triangular(Q, c, n)
            Q_lin, c_lin = lin_elim(Q, c, n)
            Q_dia, c_dia = dia_elim(Q, c, n)

            # print(np.diag(Q))
            # print(np.diag(Q_dia))