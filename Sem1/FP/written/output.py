def f(s):
    s += "has apples"

def g(n, s):
    n += 2
    s.append("apples1")
    s.append("apples2")

arr = []
number = 0
st = "Anna"
f(st)
g(number, arr)
print(st, number, arr)