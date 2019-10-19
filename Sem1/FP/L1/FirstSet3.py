'''def sortListAsc(l):
    for i in range(0,len(l)-1):
        for j in range (i+1,len(l)):
            if l[i] > l[j]:
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
    return l
'''

def listToNumber(lst):
    n=0
    for i in range(0,len(lst)):
        n=n*10+int(lst[i])
        if(lst[i-1] == '0' and lst[i] != 0):
            for j in range(0,i):
                n=n*10
    return n

lst=list(input('Give a number:'))
#lst=sortListAsc(lst)

lst.sort()
print('This is the minimal number with the same digits: ' + str(listToNumber(lst)))
