from table import makeTable
from newton import newton
import math
import matplotlib.pyplot as plt
from tabulate import tabulate

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
        ks = (math.cos((2*i+1) * math.pi / (2 * (n))))
        points.append(base+base2*ks)
    return points

def f1(x):
    return pow(math.e, math.cos(x))

def f2(x):
    return abs(x * abs(x) - 1)

a = -3
b = 3
ns = (4, 11, 21)
fs = [f1, f2]

limit = True

tabulate_arr1 = []
tabulate_arr2 = []

for j in range(0, len(fs)):
    fig, aArr2D = plt.subplots(len(ns), 2)
    for i in range(0, len(ns)):
        aArr2D[i][0].set_title("P:" + str(j + 1) + "," + str(ns[i] - 1))
        aArr2D[i][1].set_title("C:" + str(j + 1) + "," + str(ns[i] - 1))

        if limit:
            aArr2D[i][0].set_ylim(0, 10)
            aArr2D[i][1].set_ylim(0, 10)

        xs2D = [ePoints(a,b,ns[i]), chebyshow(a,b,ns[i])]
        maxp = [0, 0]
        for x in range(0, len(xs2D)):
            fxs = funcToList(xs2D[x], fs[j])
            table = makeTable(xs2D[x], fxs)
            maxpog = float(0)
            nxs = []
            nfxs = []
            nfoxs = []
            for w in range(0, 100):
                nxs.append(a + w*(b-a)/100)
                var = newton(table, nxs[w])

                diff = abs(var - fs[j](nxs[w]))
                if diff > maxpog:
                    maxpog = diff

                nfxs.append(var)
                nfoxs.append(fs[j](nxs[w]))
        
            aArr2D[i][x].plot(nxs, nfxs, label="interpolated")
            aArr2D[i][x].plot(nxs, nfoxs, label="origin")

            # print(f"max pog of {"P" if x == 0 else "C"},{j+1},{ns[i] - 1} is {maxpog}")
            maxp[x] = maxpog

            aArr2D[i][x].legend()

        if (j == 0):
            tabulate_arr1.append([ns[i] - 1, maxp[0], maxp[1]])
        else:
            tabulate_arr2.append([ns[i] - 1, maxp[0], maxp[1]])

print(tabulate(tabulate_arr1, headers=["n", "max pog of P1", "max pog of C1"], tablefmt="simple_grid"))
print(tabulate(tabulate_arr2, headers=["n", "max pog of P1", "max pog of C1"], tablefmt="simple_grid"))

plt.show()