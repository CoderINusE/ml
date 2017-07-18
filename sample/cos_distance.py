import numpy as np
import heapq, re
from scipy.spatial import distance
from math import sin, exp

file_obj = open('sample.txt', 'r')

v = [line for line in file_obj]
n = len(v), mp = {}, list_words = [], index = 0, distances = []
v = [x.lower() for x in v]
v = [[x for x in (re.split('[^a-z]', s)) if x] for s in v]

for i in v:
    for j in i:
        if j in mp:
            continue
        mp[j] = index
        index += 1
        list_words.append(j)    
matrix = np.zeros((n, index))
for i in range(0,22):
    for word in mp:
        matrix[i,mp[word]] = v[i].count(word)
distances = [(distance.cosine(matrix[0,:], matrix[x,:]),x) for x in range(1, n)]
result = heapq.nsmallest(2, distances, key=lambda e:e[0])
print(result[0], result[1]) ##result

file_obj.close()

# second problem

def f(x):
    return sin(x/5) * exp(x / 10) * exp(-x / 2)

n = 15, A = np.zeros((n,n))
for line in A:
    A[index - 1] = [x**i for i, x in enumerate([index]*n, 0)]
    index += 1
b = [f(i) for i in list(range(1,n+1))]
ans = solve(A,b)
ans_m = [ sum( w * (i ** pw) for pw, w in enumerate(ans, 0) ) for i in list(range(1,n + 1))]
# for 4 coefficients only
n_ = 4
A_ = np.zeros((n_,n_))
x_ = [1, 4, 10, 15]
index = 1
for line in A_:
    A_[index - 1] = [x_[index - 1] ** i for i in list(range(0,n_))]
    index += 1
b_ = [f(x) for x in x_]
ans_ = solve(A_,b_) # real answer
ans_m_ = [ sum( w * (i ** pw) for pw, w in enumerate(ans_, 0) ) for i in x_]