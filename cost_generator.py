## Generates Q matrix using one of 8 different methods depending on input of p
## The below methods are outlined in
## Representations of quadratic combinatorial optimization problems
## A case study using the quadratic set covering problem
## Punnen and Pandey

import numpy as np

def generate_Q(n,p,v):
    np.random.seed(2 * n + v + 11)
    n = n**2
    if (p == 1):                                            # Integers [5,10]
        Q = np.random.randint(5, high=11, size=(n, n))
    elif (p == 2):                                          # B is Integers [-5,5] matrix, Q = BB'
        B = np.random.randint(-5, high=6, size=(n, n))
        Q = np.dot(B, B.transpose())
    elif (p == 3):                                          # B is Integers [5,10] maxtrix, Q = BB'
        B = np.random.randint(5, high=11, size=(n, n))
        Q = np.dot(B, B.transpose())
    elif (p == 4):                                          # Integers [-5,5]
        Q = np.random.randint(-5, high=6, size=(n, n))
    elif (p == 5):                                          # Integers [-5,10]
        Q = np.random.randint(-5, high=11, size=(n, n))
    elif (p == 6):                                          # Integers [-10,5]
        Q = np.random.randint(-10, high=6, size=(n, n))
    elif (p == 7):
        a = np.random.randint(-10, high=11, size=(n, 1))    # a is Integers [-10,10] vector
        b = np.random.randint(-5, high=6, size=(1, n))      # b is Integers [-5,5] vector
        Q = np.outer(a, b)                                  # Q = ab
    elif (p == 8):
        a1 = np.random.randint(-10, high=11, size=(n, 1))   # a1,a2 is Integers [-10,10] vector
        a2 = np.random.randint(-10, high=11, size=(n, 1))
        b1 = np.random.randint(-5, high=6, size=(1, n))     # b1,b2 is Integers [-5,5] vector
        b2 = np.random.randint(-5, high=6, size=(1, n))
        Q = np.outer(a1, b1) + np.outer(a2, b2)             # Q = a1b1 + a2b2
    else:
        print("Not a valid choice.")
    return Q

def generate_c(n,q,v):
    np.random.seed(2 * n + v + 11)
    if (q == 1):                                            # Integers [5,10]
        c = np.random.randint(5, high=11, size=(n, n))
    elif (q == 2):                                          # B is Integers [-5,5] matrix, Q = BB'
        B = np.random.randint(-5, high=6, size=(n, n))
        c = np.dot(B, B.transpose())
    elif (q == 3):                                          # B is Integers [5,10] maxtrix, Q = BB'
        B = np.random.randint(5, high=11, size=(n, n))
        c = np.dot(B, B.transpose())
    elif (q == 4):                                          # Integers [-5,5]
        c = np.random.randint(-5, high=6, size=(n, n))
    elif (q == 5):                                          # Integers [-5,10]
        c = np.random.randint(-5, high=11, size=(n, n))
    elif (q == 6):                                          # Integers [-10,5]
        c = np.random.randint(-10, high=6, size=(n, n))
    elif (q == 7):
        a = np.random.randint(-10, high=11, size=(n, 1))    # a is Integers [-10,10] vector
        b = np.random.randint(-5, high=6, size=(1, n))      # b is Integers [-5,5] vector
        c = np.outer(a, b)                                  # Q = ab
    elif (q == 8):
        a1 = np.random.randint(-10, high=11, size=(n, 1))   # a1,a2 is Integers [-10,10] vector
        a2 = np.random.randint(-10, high=11, size=(n, 1))
        b1 = np.random.randint(-5, high=6, size=(1, n))     # b1,b2 is Integers [-5,5] vector
        b2 = np.random.randint(-5, high=6, size=(1, n))
        c = np.outer(a1, b1) + np.outer(a2, b2)             # Q = a1b1 + a2b2
    else:
        print("Not a valid choice.")
    return c