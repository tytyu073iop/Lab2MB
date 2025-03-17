import numpy

def makeTable(xArr, funcArr):
    n = len(xArr)
    table = numpy.ndarray(shape=(n,n+1))
    for i in range(0,n):
        table[i][0] = xArr[i]
        table[i][1] = funcArr[i]

    for j in range(2,n+1):
        for i in range(0,n-j+1):
            var1 = (table[i+1][j-1] - table[i][j-1])
            var2 = -(table[i][0] - table [i+j-1][0])
            table[i][j] = var1 / var2
    
    return table