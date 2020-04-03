'''Let us consider a list a1, ..., an of integer numbers.
Using Divide and Conquer compute the number of even elements from the list.'''

def even_numbers(lst):
    '''
    Compute the number of even elements from a list
    parameters:
        lst - the list of integer numbers
    return:
        return the number of even numbers
    '''
    if len(lst) == 1:
        if lst[0] % 2 == 0:
            return 1
        return 0
    else:
        middle = (len(lst))//2
        return even_numbers(lst[:middle]) + even_numbers(lst[middle:])

a = [0, 4, 7, 9, 11, 12, 16]
print(even_numbers(a))

'''
The sum of even numbers found on even positions in a list
'''


def even_sum(lst, left, right):
    '''
    Compute the sum of even numbers fround on even positions in a list
    parameters:
        lst - the list of integer numbers
        left - the index of the left bound
        right - the index of the right bound
    return:
        the sum
    '''
    if left == right:
        if lst[right] % 2 == 0 and right % 2 == 0:
            return lst[right]
        else:
            return 0
    else:
        middle = (left + right) // 2
        return even_sum(lst, left, middle) + even_sum(lst, middle + 1, right)

a = [8]
print(even_sum(a, 0, len(a)-1))