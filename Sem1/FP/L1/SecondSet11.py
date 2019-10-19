def markDigits(n):
    digits = [0] * 10
    while(n>0):
        digits[int(n)%10] = 1
        n = int(n)/10
    return digits

n1=int(input('Give a number:'))
n2=int(input('Give another number:'))
if markDigits(n1) == markDigits(n2):
    print('Your numbers have the property P (are written with the same digits)')
else:
    print('Your numbers do not have the property P (are not written with the same digits)')
