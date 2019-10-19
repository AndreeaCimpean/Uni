def divisorsSum(x):
    s=0
    for i in range(1,x):
        if x%i == 0:
            s+=i
    return s

def isPerfect(x):
    return x == divisorsSum(x) and x>1

def answer(x):
    r=0
    i=n-1
    while i > 2 and r == 0:
        if(isPerfect(i)):
            r=i
        i-=1
    return r

n=int(input('Give a number:'))
if(answer(n)):
    print('This is the largest perfect number smaller than your number: '+str(answer(n)))
else:
    print('There is no perfect number smaller than your number')

