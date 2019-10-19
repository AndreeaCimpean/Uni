'''
    Functions -> subprograms, subroutines, procedures?
    Functions:
        -Have human-readable names
        -Each function does one thing
        -Talk using parameters and/or returns
        -specification
'''

#call by value
def y(n):
    print("2",id(n))
    n=14
    print("3",id(n))

#call by reference
def x(s):
    print("2",id(s))
    #s.append(42)
    #s = []
    s += [42,43]
    print("3",id(s))

sss = []
print("1",id(sss))
x(sss)
print("4",id(sss))
print(sss)

sss = []
list.append(sss,42)
list.append(sss,43)
sss.append(44)
print(sss)

n=12
print("1",id(n))
y(n)
print("4",id(n))
