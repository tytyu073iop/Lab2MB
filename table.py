import numpy

def makeTable(xArr, funcArr):
    n = len(xArr)
    table = numpy.ndarray(shape=(n,n))
    for i in range(0,n):
        table[i][0] = xArr[i]
        table[i][1] = funcArr[i]

    for j in range(2,n):
        for i in range(0,n-j+1):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (table[i][0] - table [i+j-1][0])
    
    return table