def palindrome(n):
    '''
    Gets the palindrome of the given number
    params:
        n-the given number
    output
        the palindrome of n
    '''
    x=0
    while n > 0:
        x=x*10+int(n)%10
        n=int(n/10)
    return x

n=int(input('Give a number:'))
print('This is your number palindrome: ' + str(palindrome(n)))
