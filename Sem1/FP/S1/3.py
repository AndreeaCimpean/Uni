def stringSplosion(s):
    res = ''
    for i in range(0,len(s)):
        #print(i,s[i])
        #print(i,s[begin:end])
        res+=i,s[0:i+1]
    return res


#print(stringSplosion('python'))

s='python'
print(s[1:4])  #yth
print (s[:])   #all
print (s[4:])  #last 2
print (s[-2:]) #on
print (s[-2])  #o
print(s[1])
