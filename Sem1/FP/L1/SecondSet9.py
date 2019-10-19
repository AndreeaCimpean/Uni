def productFactors(n):
    p=1
    for d in range(2,n//2+1):
        if int(n)%d == 0:
            p*=d
    return p

n=int(input('Give a number:'))
if productFactors(n)>1:
    print('This is the product of all proper factors of your number: ' + str(productFactors(n)))
else:
    print('Your number does not have proper factors')
