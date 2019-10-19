def isPrime(x):
    '''
    Validates if the given number is prime
    params:
        x-the given number
    output
        True - if x is prime
        False - if x is not prime
    '''
    if x<=1:
        return False
    else:
        for d in range(2,x//2+1):
            if int(x)%d == 0:
                return False
        return True
    
def getNextPrimeNumber(x):
    '''
    Gets the smallest prime number larger than the given number
    params:
        n-the given number
    output
        the next prime number
    '''
    if x<=1:
        return 2
    else:
        answer=x+1
        while(not isPrime(answer)):
            answer+=1
    return answer
        
n=int(input('Give a number:'))
print('This is the next prime number: '+str(getNextPrimeNumber(n)))

