def isPrime(x):
    if x <= 1:
        return False
    else:
        for d in range(2,x//2+1):
            if int(x)%d == 0:
                return False
        return True

def goldbach(x):
    i = 2
    j = x-2
    l=[]
    while len(l) == 0:
        if isPrime(i) and isPrime(j):
            l+=[i,j]
        i+=1
        j-=1
    return l

n=int(input('Give a number:'))
if n<=2:
    print('Your number cannot be written as sum of two prime numbers')
else:
    l=goldbach(n)
    print(str(n) + ' can be written as sum of the following prime numbers: ' + str(l[0]) + '+' +str(l[1]))
    
