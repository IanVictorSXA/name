def sum(n):
    a = 0.171
    num = 0
    for i in range(n):
        num += a*pow(1-a,i)

    return num
