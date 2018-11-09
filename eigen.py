import numpy as np

for n in range(5,35,5):
    for p in range(1,9):
        Q = np.loadtxt('qap-n''%s''p''%s''.txt' %(n,p))
        c = np.loadtxt('cap-n''%s''p''%s''.txt' %(n,p))

        w,v = np.linalg.eig(Q)

        print(min(abs(w)))