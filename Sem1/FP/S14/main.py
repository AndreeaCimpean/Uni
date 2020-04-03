'''
an array
len = n
6 -2 -3 1 5 -2 -1 2
subarray - consecutive
'''

data = [6, -2, -3, 1, 5, -2, -1, 2, -9]

# 9th grade
# time complexity O(n^3)
def maxSum1(arr):
    # global = best I've seen do far 
    # local = best right now
    global_sum = arr[0]  # don't initialize with 'random' number
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            local_sum = sum(arr[i:j])
            if local_sum > global_sum:
                global_sum = local_sum
    return global_sum

print(maxSum1(data))
            
# 10th grade
# time complexity O(n^2)
def maxSum2(arr):
    # global = best I've seen do far 
    # local = best right now
    global_sum = arr[0]  # don't initialize with 'random' number
    for i in range(len(arr)):
        local_sum = arr[i]
        if local_sum > global_sum:
            global_sum = local_sum
        for j in range(i + 1, len(arr)):
            local_sum += arr[j]
            if local_sum > global_sum:
                global_sum = local_sum
    return global_sum

print(maxSum2(data))


# 11th grade 
# divide and conquer
# time complexity O(nlogn)
# T(n) = 1, n = 1
#        2T(n/2) + n <- contains middle
#           ^
#           |
#        in left
#        in right

# this is O(n)
def dcMiddle(arr, low, high):
    m = (low+high)//2
    # for loop with partial sums between low and m
    # for loop with partial sums between m and high
    # add max partial sum in left half to right half with arr[m] and return it

# this is O(nlogn)
def maxSum3(arr, low, high):
    if low == high:
        return arr[0]
    m = (low+high)//2
    return max(maxSum3(arr, low, m), maxSum3(arr, m + 1, high), dcMiddle(arr, low, high))

# print(maxSum3(data, 0, len(data)))


# 12th grade
# dynamic programming 
# time complexity O(n)
def maxSum4(arr):
    # memorization is in max_local
    max_local = arr[0]
    max_global = arr[0]
    for i in range(1, len(arr)):
        # overalapping subproblems
        max_local = max(arr[i], arr[i] + max_local)
        max_global = max(max_global, max_local)
    return max_global
print(maxSum4(data))

s1 =  'abcd'
s2 = 'axd'

'''
    transform s1 -> s2
    character by character, start from the end
'''
def xform(s1, s2):
    # ine string is empty
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    elif s1[-1] == s2[-1]:
        return xform(s1[:-1], s2[:-1])
    # gr8 what now?
    return 1 + min(
    xform(s1[:-1], s2),  # delete last character from s1
    xform(s1[:-1], s2[:-1]),  # replace last character in s1
    xform(s1, s2[:-1])  # insert character at the end of s1
    )
print(xform(s1, s2))

# dynamic programming -> tree -> matrix