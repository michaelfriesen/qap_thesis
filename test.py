from equivalent_rep import *
from gurobi_model import *
from reading import *

p = 6
n = 5
v = 7



# Run original model
Q,c = read_matrix(n,p,v)

Q_pos, c_pos = positive(Q, c, n)
Q_neg, c_neg = negative(Q, c, n)
Q_tri, c_tri = triangular(Q, c)

# m, x = gur_build_model(Q, c, n)
#
# m = gur_set_obj(Q, c, m, x, n)
# t1, z1 = gur_optimize(m)

kl_list = [(0,4),(1,2),(2,0),(3,3),(4,1)]
ij_list = [(0,0),(1,4),(2,2),(3,1),(4,3)]

c_sum = 0
Q_sum = 0
for (i,j) in ij_list:
    c_sum += c[i,j]
    for (k,l) in ij_list:
        Q_sum += Q[(i*n)+j,(k*n)+l]
print(c_sum+Q_sum)

# c_sum = 0
# Q_sum = 0
# for (i,j) in kl_list:
#     c_sum += c[i,j]
#     for (k,l) in kl_list:
#         Q_sum += Q[(i*n)+j,(k*n)+l]
# print(c_sum+Q_sum)

c_sum = 0
Q_sum = 0
for (i,j) in kl_list:
    c_sum += c_pos[i,j]
    for (k,l) in kl_list:
        Q_sum += Q_pos[(i*n)+j,(k*n)+l]
print(c_sum+Q_sum)

c_sum = 0
Q_sum = 0
for (i,j) in kl_list:
    c_sum += c_neg[i,j]
    for (k,l) in kl_list:
        Q_sum += Q_neg[(i*n)+j,(k*n)+l]
print(c_sum+Q_sum)

c_sum = 0
Q_sum = 0
for (i,j) in ij_list:
    c_sum += c_tri[i,j]
    for (k,l) in ij_list:
        Q_sum += Q_tri[(i*n)+j,(k*n)+l]
print(c_sum+Q_sum)

# print(Q-Q_tri)

# print(z1)