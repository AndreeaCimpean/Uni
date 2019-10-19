def evenNumbers(lst):
    count = 0
    for i in lst:
        if i%2 == 0:
            count+=1
    return count

#empty list
data = list(range(20))
print(data)
print(data[2:6])

print(evenNumbers(data))
