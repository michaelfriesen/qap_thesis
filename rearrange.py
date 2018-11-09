## Takes Q matrix and row or column index then returns n x n matrix corresponding to the row or column
## Useful for checking row/column elimination function is giving proper results

def rearrange_row(Q,n,i):
    QQ = Q[i,:].reshape(n,n)
    return QQ

def rearrange_col(Q,n,j):
    QQ = Q[:,j].reshape(n,n)
    return QQ