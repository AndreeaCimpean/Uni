'''
insertion sort
     - add each element into its correct place in a sorted list
'''

import random


'''
n = len(data)
AC x
WC T(n) = sum(i=1,n)i = 1+2+3+...+n = n*(n+1)/2 apartine O(n^2)
'''
def insertSort(data):
    for i in range(1, len(data)):  # data[0:i] is already sorted
        elem = data[i]  # current element to move
        # figure out where to move elem
        j = i - 1
        while j >= 0 and data[j] > elem:
            data[j+1] = data[j]
            j -= 1

        # insert the element in the correct place
        data[j+1] = elem


'''
merge sort
    - divide the list into halves
    - sort the halves :)
    - merge the two halves (merge = interclasare)

T(n) = 1, n=1
       2*T(n/2) + n/2 + n/2
T(n) apartine O(nlog2(n))
'''


def merge(data1, data2):
    sorted_list = []
    i = 0
    j = 0
    while i < len(data1) and j < len(data2):
        if data1[i] < data2[j]:
            sorted_list += data1[i]
            i += 1
        else:
            sorted_list += data2[j]
            j += 1
    while i < len(data1):
        sorted_list += data1[i]
        i += 1
    while j < len(data2):
        sorted_list += data2[j]
        j += 1

    return sorted_list




def mergeSort(data):
    m = len(data) // 2
    left = mergeSort(data[:m])  # extra list copying on the side
    right = mergeSort(data[m:])
    return merge(left, right)


data = list(range(10))
random.shuffle(data)
print(data)
insertSort(data)
print(data)