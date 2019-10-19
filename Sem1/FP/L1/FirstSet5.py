def isPrime(n):
    if n <= 1:
        return False
    else:
        for d in range(2,n//2+1):
            if int(n)%2 == 0:
                return False
        return True

def smallerPrime(n):
    if n <= 2:
        return 0
    else:
        i = n-1
        while i > 1:
            if isPrime(i):
                return i
            i-=1

n=int(input('Give a number:'))
if(smallerPrime(n)):
    print('This is the largest prime number smaller than your number: ' + str(smallerPrime(n)))
else:
    print('There is no prime number smaller than your number')
