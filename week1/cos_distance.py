import numpy as np
import heapq, re
from scipy.spatial import distance

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