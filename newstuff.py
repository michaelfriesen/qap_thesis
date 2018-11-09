import numpy as np
from gurobipy import *

n = 2
M = 1000

z1=0
z2=0

while z1 == z2:
    Q = np.random.randint(-5, high=6, size=(n**2, n**2))
    c = np.random.randint(-5, high=6, size=(n, n))

    # print(Q)
    # print(c)

    m = Model()

    m.Params.OutputFlag = False
    m.Params.timeLimit = 10800

    x = m.addVars(n, n, vtype=GRB.BINARY, name="x")

    m.addConstrs(x.sum(i, '*') == 1 for i in range(n))
    m.addConstrs(x.sum('*', j) == 1 for j in range(n))

    m.setObjective(sum(Q[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in range(n) for l in range(n)) + sum(c[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)
    m.optimize()

    z1 = m.ObjVal
    x1 = [(v.varName, v.X) for v in m.getVars() if abs(v.obj) > 1e-6 if v.X > 1e-6]

    Q = Q + M*np.diag(np.ones(n**2))
    c = c - M*np.ones((n,n))

    m.setObjective(sum(
    Q[(i * n) + j, (k * n) + l] * x[i, j] * x[k, l] for i in range(n) for j in range(n) for k in range(n) for l in
    range(n)) + sum(c[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)
    m.optimize()

    z2 = m.ObjVal
    x2 = [(v.varName, v.X) for v in m.getVars() if abs(v.obj) > 1e-6 if v.X > 1e-6]

    # print(m.ObjVal)
    # print([(v.varName, v.X) for v in m.getVars() if abs(v.obj) > 1e-6 if v.X > 1e-6])

print(Q)
print(c)
print(x1)
print(x2)