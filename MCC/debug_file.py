
import numpy as np


a = np.array([[25088.596,  4427.3994,  4427.3994,  0.0, 0.0, 0.0],
             [4427.3994,   25088.596, 4427.3994,  0.0, 0.0, 0.0],
             [4427.3994,    4427.3994, 25088.596, 0.0, 0.0, 0.0],
             [0.0,      0.0,    0.0,  10330.5987, 0.0, 0.0],
             [0.0,      0.0,    0.0,   0.0,     10330.5987, 0.0],
             [0.0,      0.0,    0.0,   0.0,     0.0,     10330.5987 ]])

b = np.array([[180.30848],
              [43.71221395],
              [43.71221395],
              [0.0],
              [0.0],
              [0.0]])

c = np.dot(a,b)
d = b.transpose()

e = np.dot(d,a)

NR = np.dot(c,e)

# print(d)
# print(e)
# print(NR)

f = np.array([[-1912913.30886075],
              [-1912913.30886075],
              [-1912913.30886075],
               [0.0],
               [0.0],
               [0.0]])
f_trans = f.transpose()
g = np.dot(d,b)

h = (-1.0)*np.dot(f_trans,b)

DR = h+g

i = NR/DR

FINAL = a-i

print(FINAL)