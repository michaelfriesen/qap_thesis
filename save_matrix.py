from cost_generator import *
import numpy as np

# save_path = "C:\Users\Michael\Desktop\QAP\Cost Matrices"

# random seed = 2n + v + 11

n = 15

for p in range(1,9):
    for v in range(5,10):
        Q = generate_Q(n,p,v)
        c = generate_c(n,p,v)
        np.savetxt('qap-n''%s''p''%s''-''%s''.txt' %(n,p,v),Q)
        np.savetxt('cap-n''%s''p''%s''-''%s''.txt' % (n,p,v), c)

n=20

for p in range(1,9):
    for v in range(0,5):
        Q = generate_Q(n,p,v)
        c = generate_c(n,p,v)
        np.savetxt('qap-n''%s''p''%s''-''%s''.txt' %(n,p,v),Q)
        np.savetxt('cap-n''%s''p''%s''-''%s''.txt' % (n,p,v), c)
