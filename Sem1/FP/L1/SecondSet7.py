def isPrime(n):
    if n <= 1:
        return False
    else:
        for d in range(2,n//2+1):
            if int(n)%d == 0:
                return False
        return True

def answer(n):
    p=n+1
    found=False
    while(not found):
        if isPrime(p) and isPrime(p+2):
            found=True
        p+=1
    return p-1

n=int(input('Give a number:'))
print('These are the prime twin numbers immediately larger than your number: ' + str(answer(n)) + ',' + str(answer(n)+2))
