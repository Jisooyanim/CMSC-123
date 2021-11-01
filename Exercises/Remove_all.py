def valid_input(input, mode):
    if mode == 0:#For array size
        if input <= 0:
            return False
        else:
            return True
    elif mode == 1:#For type
        if input == "Numeric":
            return 1
        elif input == "String":
            return 2
        else:
            return 0
    elif mode == 2:#For condition
        if input == "==" or input == "<" or input == ">" or input == ">=" or input == "<=" or input == "!=":
            return 1
        else:
            return 0

def remove_all(A, x, condition):
    if condition == "==":
        for i in range(len(A) - 1, -1, -1):
            if A[i] == x:
                A.pop(i)
    elif condition == ">":
        for i in range(len(A) - 1, -1, -1):
            if A[i] > x:
                A.pop(i)
    elif condition == "<":
        for i in range(len(A) - 1, -1, -1):
            if A[i] < x:
                A.pop(i)
    elif condition == ">=":
        for i in range(len(A) - 1, -1, -1):
            if A[i] >= x:
                A.pop(i)
    elif condition == "<=":
        for i in range(len(A) - 1, -1, -1):
            if A[i] <= x:
                A.pop(i)
    elif condition == "!=":
        for i in range(len(A) - 1, -1, -1):
            if A[i] != x:
                A.pop(i)

def print_array(arr):
    if len(arr) == 0:
        print(" ")
    else:
        for i in range(0, len(arr)):
            print(arr[i], end = " ")

arr_size = int(input())
if valid_input(arr_size, 0) == False:
    quit()
type = input()
if valid_input(type,1) == 0:
    quit()
if valid_input(type, 1) == 1:
    array = list(int(arr) 
    for arr in input().strip().split())[:arr_size]
    condition = input()
    if valid_input(condition, 2) == 0:
        quit()
    x = int(input())
    remove_all(array, x, condition)
    print_array(array)

elif valid_input(type,1) == 2:
    array = list(str(arr) 
    for arr in input().strip().split())[:arr_size]
    condition = input()
    if valid_input(condition, 2) == 0:
        quit()
    x = input()
    remove_all(array, x, condition)
    print_array(array)  