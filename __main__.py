from equivalent_rep import *
from gurobi_model import *
from reading import *
from gurobipy import *

# for p in range(1,9):
#    for n in range(5,20,5):
#        for v in range(0,10):
for p in range(1,9):
    for v in range(0,10):
        for n in range(15,25,5):
            if (n == 15 and v < 5):
                continue
            if (n == 20 and v > 0):
                continue

            # Run original model
            Q,c = read_matrix(n,p,v)
            Q_dia, c_dia = dia_elim(Q,c,n)
            Q_lin, c_lin = lin_elim(Q,c,n)
            # Q_sym, c_sym = symmetry(Q, c)
            Q_pos, c_pos = positive(Q, c, n)
            Q_neg, c_neg = negative(Q, c, n)
            Q_tri, c_tri = triangular(Q, c, n)
            m, x = gur_build_model(Q, c, n)

            # m.setParam('TimeLimit',10)

            # z = Q.max() * n * n

            # m = gur_set_obj(Q, c, m, x, n)
            # # m.addConstr(sum(Q[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in range(n) for l in range(n)) + sum(c[i, j] * x[i, j] for i in range(n) for j in range(n)) <= -95)
            # t1, z1 = gur_optimize(m)
            # print([(v.varName, v.X) for v in m.getVars() if abs(v.X) > 0.5])

            # m = gur_set_obj(Q_sym, c_sym, m, x, n)
            # m.addConstr(sum(
            #     Q_sym[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in range(n)
            #     for l in range(n)) + sum(c_sym[i, j] * x[i, j] for i in range(n) for j in range(n)) <= -95)
            # t2, z2 = gur_optimize(m)

            m = gur_set_obj(Q_dia, c_dia, m, x, n)
            t2, z2 = gur_optimize(m)
            # print([(v.varName, v.X) for v in m.getVars() if abs(v.X) > 0.5])

            m = gur_set_obj(Q_lin, c_lin, m, x, n)
            t3, z3 = gur_optimize(m)
            # print([(v.varName, v.X) for v in m.getVars() if abs(v.X) > 0.5])

            m = gur_set_obj(Q_pos, c_pos, m, x, n)
            t4, z4 = gur_optimize(m)
            # print([(v.varName, v.X) for v in m.getVars() if abs(v.X) > 0.5])

            m = gur_set_obj(Q_neg, c_neg, m, x, n)
            t5, z5 = gur_optimize(m)
            # print([(v.varName, v.X) for v in m.getVars() if abs(v.X) > 0.5])

            m = gur_set_obj(Q_tri, c_tri, m, x, n)
            t6, z6 = gur_optimize(m)
            # print([(v.varName, v.X) for v in m.getVars() if abs(v.X) > 0.5])

            m = gur_set_obj(Q, c, m, x, n)
            t1, z1 = gur_optimize(m)
            # print([(v.varName, v.X) for v in m.getVars() if abs(v.X) > 0.5])

            # z = min(z1,z2,z3,z4,z5)
            z = min(z1, z2, z3, z4, z5, z6)

            z_test = 0
            if (z1 == z) and (z2 == z) and (z3 == z) and (z4 == z) and (z5 == z) and (z6 == z):
            # if (z1==z) and (z2==z) and (z3==z) and (z4==z) and (z5==z):
                z_test = 1
            else:
                z_test = 0

#            printing_line = z_test & " qap-n" & n & "p" & "p" & "v" & v & " " & n & " " & z1 & " " & z2 & " " & z3 & " " & z4 & " " & z5 & " " & z6 & " " & t1 & " " & t2 & " " & t3 & " " & t4 & " " & t5 & " " & t6
            
            # print('%s'' qap-n''%s''p''%s''v''%s %s %s %s %s %s %s %s %s %s %s %s' % (z_test,n, p, v, n, z1, z2, z3, z4, z5, t1, t2, t3, t4, t5))
    #        print('%s'' qap-n''%s''p''%s''v''%s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (z_test, n, p, v, n, z1, z2, z3, z4, z5, z6, t1, t2, t3, t4, t5, t6))
    #        print(printing_line)
            with open('_______Results.txt', 'a') as the_file:
                the_file.write('%s'' qap-n''%s''p''%s''v''%s %s %s %s %s %s %s %s %s %s %s %s %s %s\n' % (z_test, n, p, v, n, z1, z2, z3, z4, z5, z6, t1, t2, t3, t4, t5, t6))

    
            # if (z1 != z) or (z2 != z) or (z3 != z) or (z4 != z) or (z5 != z):
            #     print('qap-n''%s''p''%s''v''%s %s %s %s %s %s %s' % (n, p, v, n, z1, z2, z3, z4, z5))
            #     # print('qap-n''%s''p''%s''v''%s %s %s %s %s %s %s %s %s %s %s %s' % (n, p, v, n, z1, z2, z3, z4, z5, t1, t2, t3, t4, t5))
            # else:
            #     print('qap-n''%s''p''%s''v''%s' % (n, p, v))

            # while (z1 != z) or (z2 != z) or (z3 != z) or (z4 != z) or (z5 != z):
            #
            #     # print(z, z1, z2, z3, z4, z5)
            #
            #     if z1 > z:
            #         m = gur_set_obj(Q, c, m, x, n)
            #         m.addConstr(sum(
            #             Q[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in
            #             range(n) for l in range(n)) + sum(c[i, j] * x[i, j] for i in range(n) for j in range(n)) <= z, "UB")
            #         t1, z1 = gur_optimize(m)
            #     if z2 > z:
            #         m = gur_set_obj(Q_sym, c_sym, m, x, n)
            #         m.addConstr(sum(
            #             Q_sym[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in
            #             range(n) for l in range(n)) + sum(c_sym[i, j] * x[i, j] for i in range(n) for j in range(n)) <= z, "UB")
            #         t2, z2 = gur_optimize(m)
            #         # m.remove(m.getConstrs()[-1])
            #     if z3 > z:
            #         m = gur_set_obj(Q_pos, c_pos, m, x, n)
            #         m.addConstr(sum(
            #             Q_pos[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in
            #             range(n) for l in range(n)) + sum(c_pos[i, j] * x[i, j] for i in range(n) for j in range(n)) <= z, "UB")
            #         t3, z3 = gur_optimize(m)
            #         # m.remove(m.getConstrs()[-1])
            #     if z4 > z:
            #         m = gur_set_obj(Q_neg, c_neg, m, x, n)
            #         m.addConstr(sum(
            #             Q_neg[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in
            #             range(n) for l in range(n)) + sum(c_neg[i, j] * x[i, j] for i in range(n) for j in range(n)) <= z, "UB")
            #         t4, z4 = gur_optimize(m)
            #         # m.remove(m.getConstrs()[-1])
            #     if z5 > z:
            #         m = gur_set_obj(Q_tri, c_tri, m, x, n)
            #         m.addConstr(sum(
            #             Q_tri[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in
            #             range(n) for l in range(n)) + sum(c_tri[i, j] * x[i, j] for i in range(n) for j in range(n)) <= z, "UB")
            #         t5, z5 = gur_optimize(m)
            #         # m.remove(m.getConstrs()[-1])
            #
            #     z = min(z1,z2,z3,z4,z5)
            #
            # print('qap-n''%s''p''%s''v''%s %s %s %s %s %s %s' % (n, p, v, n, z1, z2, z3, z4, z5))
