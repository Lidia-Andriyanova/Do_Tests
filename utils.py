# Перевод в двоичную систему
def to_binary(n):
    res = ''
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return int(res)


# Числа Негафибоначчи
def neg_fib(num):
    lst = []
    if num >= 1:
        lst.append(1)
    if num >= 2:
        lst.append(-1)
    for i in range(2, num):
        lst.append(lst[i -2] - lst[i - 1])
    res = []
    for elem in lst:
        res.insert(0, elem)
    return res



