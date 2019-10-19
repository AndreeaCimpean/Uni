def isPrime(n):
    if n<=1:
        return False
    else:
        for d in range(2,n//2+1):
            if int(n)%d == 0:
                return False
        return True
    
def answer(n):
    if n == 1:
        return 1
    else:
        position = 1
        nr = 2
        found = 0
        while found == 0:
            if(isPrime(nr)):
                position+=1
                if position == n:
                    found = nr
            else:
                div = 2
                cnr = nr
                while cnr>1 and found == 0:
                    if int(cnr)%div == 0:
                        while int(cnr)%div == 0:
                            cnr = int(cnr)/div
                        position+=div
                    if position >= n:
                        found = div
                    else:
                        div+=1
            nr+=1
        return found
    

n=int(input('Give a number:'))
print('This is the number in the sequence: ' + str(answer(n)))
