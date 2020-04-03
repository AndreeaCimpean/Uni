def consistent(x, n):
    if len(x) > 1:
        for i in range(0, len(x)-1):
            if x[i] == x[len(x) - 1]:
                return False
    if len(x) > n:
        return False
    return True

def solution(x, n):
    if len(x) == n:
        return True
    return False

def display(x):
    s = ""
    for i in x:
        s += str(i)
    print(s)

def backtracking(x, n):
    x.append(0)
    for i in range(1, n + 1):
        x[-1] = i
        if consistent(x, n):
            if solution(x, n):
                display(x)
            backtracking(x[:], n)

a = []
backtracking(a, 4)