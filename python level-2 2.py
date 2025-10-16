mat=[[1,2,3],[4,5,6],[7,8,9]]
d=[mat[i][i] for i in range(len(mat))]
print("diagonal elements are",*d)
print("sum of diagonal elements=",sum(d))
