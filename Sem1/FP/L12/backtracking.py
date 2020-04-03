'''
The sequence a = 𝑎1, …, 𝑎𝑛 with distinct integer numbers is given. 
Determine all subsets of elements having the sum divisible by a given n.
'''

def valid(level, solution_array, length):
    if solution_array[level] <= solution_array[level - 1] and level > 0:
        return False
    if level >= length:
        return False
    return True

def solution(n, solution_array, level):
    s = 0
    for i in range(0, level + 1):
        s += solution_array[i]
    return s%n == 0

def display(solution_array, level):
    display_list = ""
    for i in range(0, level + 1):
        display_list += str(solution_array[i]) 
        display_list += ' '
    print(display_list)

def BacktrackingRecursive(solution_array, level, listNumbers,  n):
    for i in range(0, len(listNumbers)):
        solution_array[level] = listNumbers[i]
        if valid(level, solution_array, len(listNumbers)):
            if solution(n, solution_array, level):
                display(solution_array, level)
            BacktrackingRecursive(solution_array, level + 1, listNumbers, n)

def BacktrackingIterative(solution_array, listNumbers,  n):
    level = 0
    index = 0
    index_before_level_up = [0] * len(listNumbers)
    while level != -1:
        solution_array[level] = listNumbers[index]
        if valid(level, solution_array, len(listNumbers)):
            if solution(n, solution_array, level):
                display(solution_array, level)
            index_before_level_up[level] = index
            level += 1
            index = 0
        elif index < len(listNumbers) - 1 and level < len(listNumbers):
            index += 1
        else:
            level -= 1
            if level != -1:
                index = index_before_level_up[level] + 1 
                while level != -1 and index == len(listNumbers):
                    level -= 1
                    if level == -1:
                        break
                    index = index_before_level_up[level] + 1 

def read_list():
    listNumbers = []
    listNumbers = input("the list: ").split(" ")
    for i in range(len(listNumbers)):
        listNumbers[i] = int(listNumbers[i])
    return listNumbers

def main():
    a = read_list()
    n = int(input("the number: "))
    solution_array = [0] * (len(a) + 1)
    print("RECURSIVE")
    BacktrackingRecursive(solution_array, 0, a, n)
    print("ITERATIVE")
    BacktrackingIterative(solution_array, a, n)

main()