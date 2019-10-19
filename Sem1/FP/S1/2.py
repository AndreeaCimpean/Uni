'''def f(x,y):
    return x == 10 or y == 10 or x+y == 10
#How do we make the program user-proof?
a=int(input('Give a='))
b=int(input('Give b='))

print(f(a,b))'''

def sleepIn(weekday, vacation):
    '''
Function decides wether we are sleeping in
input:
    weekday - True if it is a weekday
    vacation - True if we are sleeping in
output:
    True if we are sleeping in
exception:
    -
    '''
    return vacation or not weekday

#print((sleepIn(True,True))

weekday=input('Is it a weekday(yes/no)')
if weekday=='yes':
    weekday=True
else:
    weekday=False

vacation=input('Is it a vacation(yes/no)')
if vacation=='yes':
    vacation=True
else:
    vacation=False

print((sleepIn(weekday,vacation)
