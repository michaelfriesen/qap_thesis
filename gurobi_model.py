from gurobipy import *

def gur_build_model(Q,c,n):
    m = Model()

    # m.Params.OutputFlag = False
    m.Params.timeLimit = 10800
    # m.Params.timeLimit = 1
    # m.Params.BestObjVal = -54.0
    x = m.addVars(n, n, vtype=GRB.BINARY, name="x")

    m.addConstrs(x.sum(i, '*') == 1 for i in range(n))
    m.addConstrs(x.sum('*', j) == 1 for j in range(n))

    m.setObjective(sum(
        Q[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in range(n) for l in
        range(n))
                   + sum(c[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    return m,x

def gur_optimize(m):
    m.optimize()
    t = m.Runtime
    z = m.ObjVal
    return t,z

def gur_set_obj(Q,c,m,x,n):
    m.setObjective(sum(
        Q[i * n + j, k * n + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in range(n) for l in
        range(n))
                   + sum(c[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)
    return m
