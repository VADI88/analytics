import math as m
A = 270 # A must not be 1 because then infinite operations can occur, sqrt(1) = 1
B = 290
nops = 0
a = m.ceil(m.sqrt(A))
b = m.floor(m.sqrt(B))
while b >= a:
    a = m.ceil(m.sqrt(a))
    b = m.floor(m.sqrt(b))
print([A, B, nops])

