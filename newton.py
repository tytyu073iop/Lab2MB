

def newton(table, x):
    n = table.shape[1]

    sum = float(0)

    for i in range(1,n):
        num = table[0][i]
        for j in range(0, i-1):
            num *= (x - table[j][0])
        sum += num
    
    return sum