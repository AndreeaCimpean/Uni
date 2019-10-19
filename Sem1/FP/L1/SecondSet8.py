def Fibonacci(n):
    f1=1
    f2=1
    while(f2<=n):
        aux=f2
        f2=f1+f2
        f1=aux
    return f2

n=int(input('Give a number:'))
print('This is the smallest number from the Fibonacci sequence larger than your number: ' + str(Fibonacci(n)))
