

def newton(table, x):
    n = table.shape[0]

    sum = float(0)

    for i in range(1,n):
        num = table[0][i]
        for j in range(0, i-1):
            num *= (x - table[0][j])
        sum += num
    
    return sum