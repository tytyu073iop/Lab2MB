from table import makeTable
from newton import newton
import math
import matplotlib.pyplot as plt

def ePoints(a,b,n):
    points = [a]
    div = (b-a)/(n-1)
    for i in range(1, n):
        points.append(a + div*i)

    return points

def funcToList(list, func):
    l = []
    for i in list:
        l.append(func(i))
    return l

def chebyshow(a,b,n):
    points = []
    base = (a + b)/2
    base2 = (b - a)/2
    x = base
    for i in range(0,n):
        ks = (math.cos((2*i+1) / (2 * (n))))
        points.append(base+base2*ks)
    return points

def f1(x):
    return pow(math.e, math.cos(x))

def f2(x):
    return abs(x * abs(x) - 1)

a = -3
b = 3
ns = (3, 10, 20)
fs = [f1, f2]

for j in range(0, len(fs)):
    fig, aArr2D = plt.subplots(len(ns), 2)
    for i in range(0, len(ns)):
        aArr2D[i][0].set_title("P:" + str(j + 1) + "," + str(ns[i]))
        aArr2D[i][1].set_title("C:" + str(j + 1) + "," + str(ns[i]))

        xs2D = [ePoints(a,b,ns[i]), chebyshow(a,b,ns[i])]
        for x in range(0, len(xs2D)):
            fxs = funcToList(xs2D[x], fs[j])
            table = makeTable(xs2D[x], fxs)
            maxpog = float(0)
            nxs = []
            nfxs = []
            nfoxs = []
            for w in range(0, 100):
                nxs.append(a + w*(b-a)/100)
                nfxs.append(newton(table, nxs[w]))
                nfoxs.append(fs[j](nxs[w]))
        
            aArr2D[i][x].plot(nxs, nfxs, label="interpolated")
            aArr2D[i][x].plot(nxs, nfoxs, label="origin")

            aArr2D[i][x].legend()

plt.show()