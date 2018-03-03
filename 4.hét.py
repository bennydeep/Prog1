import numpy as np
import time

v = np.arange(10, 50)


def reverse(v):
    newV = np.zeros(v.size, dtype='int32')
    for i in range(v.size - 1, -1, -1):
        newV[v.size - 1 - i] = (v[i])
    return newV


# v=v[::-1]
print(v)
vmod = reverse(v)
print(vmod)
# print (v.size)
# print (v.ndim)
# print (v.dtype)
# print (v.shape)


import numpy as np


def indexofminmax(v):
    minv = 101
    maxv = -1
    minlist = []
    maxlist = []
    for i in range(0, v.size):
        if minv[i] > v[i]:
            minv = v[i]
            minlist = []
            minlist.append(i)
        elif minv == v[i]:
            minlist.append(i)
        if maxv > v[i]:
            maxv = v[i]
            maxlist = []
            max.append(i)
        elif maxv == v[i]:
            maxlist.append(i)
    return maxlist + minlist


v = np.round(100 * np.random.random(30))
incides = indexofminmax(v)
print(v)



def sortvector(v):
    for i in range(0, v.size):
        for j in range(i + 1, v.size):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v


v = np.random.randint(10, 130, 100)
vsorted = sortvector(v.copy())
print(v)
print(vsorted)

v.sort





def sortvector(v):
    for i in range(0, v.size):
        for j in range(i + 1, v.size):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v


v = np.random.randint(10, 130, 10000)
start = time.time()
# vsorted=sortvector(v.copy())
v.sort()
during = time.time() - start
print(v)
print(during)