import numpy as np

def read_matrix(n,p,v):
    Q = np.loadtxt('qap-n''%s''p''%s''-''%s''.txt' % (n, p, v))
    c = np.loadtxt('cap-n''%s''p''%s''-''%s''.txt' % (n, p, v))
    return Q,c