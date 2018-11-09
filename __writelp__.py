from equivalent_rep import *
from gurobi_model import *
from reading import *
from gurobipy import *

for p in range(1,9):
    for v in range(0,10):
        for n in range(5,15,5):
        
            # Run original model
            Q,c = read_matrix(n,p,v)
            Q_dia, c_dia = dia_elim(Q,c,n)
            Q_lin, c_lin = lin_elim(Q,c,n)
            # Q_sym, c_sym = symmetry(Q, c)
            Q_pos, c_pos = positive(Q, c, n)
            Q_neg, c_neg = negative(Q, c, n)
            Q_tri, c_tri = triangular(Q, c, n)
            m, x = gur_build_model(Q, c, n)
            
            m = gur_set_obj(Q_dia, c_dia, m, x, n)
            m.write('dia-n''%s''p''%s''v''%s''.lp' % (n, p, v))
            
            m = gur_set_obj(Q_lin, c_lin, m, x, n)
            m.write('lin-n''%s''p''%s''v''%s''.lp' % (n, p, v))
            
            m = gur_set_obj(Q_pos, c_pos, m, x, n)
            m.write('pos-n''%s''p''%s''v''%s''.lp' % (n, p, v))

            m = gur_set_obj(Q_neg, c_neg, m, x, n)
            m.write('neg-n''%s''p''%s''v''%s''.lp' % (n, p, v))
            
            m = gur_set_obj(Q_tri, c_tri, m, x, n)
            m.write('tri-n''%s''p''%s''v''%s''.lp' % (n, p, v))
            
            m = gur_set_obj(Q, c, m, x, n)
            m.write('ori-n''%s''p''%s''v''%s''.lp' % (n, p, v))
           
