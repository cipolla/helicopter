import numpy as np
from pylab import *
#import miles_aoa as fun
import math

# GLOBAL VARIABLES
lamb = 0.5
theta0 = []
alpha = []
X = []
Y = []
Cl_nc = []
w0 = 5
v = 5
ds = 0.01
A1 = 0.165*2
b1 = 0.0455
A2 = 0.335*2
b2 = 0.3

s = np.arange(0, 6, ds)

#Array of theta0
for ele in s:
    x0 = ele/(2*math.fabs(lamb))
    if x0 > 1:
        x0 = 1
    theta0.append(math.acos(1-2*x0))

#Array of alpha
for ele in theta0:
    alpha.append((ele + sin(ele))/math.pi*w0/v)

#Circulatory lift Cl_c
for n in range(len(s)):
    if n == 0:
        X.append(0)
        Y.append(0)
        Cl_nc.append(0)
    else:
        X.append(X[n-1]*exp(-b1*ds)+A1*(alpha[n]-alpha[n-1]))
        Y.append(Y[n-1]*exp(-b2*ds)+A2*(alpha[n]-alpha[n-1]))
        Cl_nc.append(((sin(2*theta0[n])*0.5-theta0[n]) - (sin(2*theta0[n-1])*0.5-theta0[n-1]))/ds*(-0.5)*w0/v)

Cl_t = [a-b-c+d for a, b, c, d in zip(alpha, X, Y, Cl_nc)]
#print(Cl_c)

#Non-circulatory lift Cl_nc





plot(s, Cl_t)
show()
