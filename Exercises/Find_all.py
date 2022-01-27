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


def find_all(A, x, condition):
    B = []
    if condition == "==":
        for i in range(len(A)):
            if A[i] == x:
                B.append(i)
    elif condition == ">":
        for i in range(len(A)):
            if A[i] > x:
                B.append(i)
    elif condition == "<":
        for i in range(len(A)):
            if A[i] < x:
                B.append(i)
    elif condition == ">=":
        for i in range(len(A)):
            if A[i] >= x:
                B.append(i)
    elif condition == "<=":
        for i in range(len(A)):
            if A[i] <= x:
                B.append(i)
    elif condition == "!=":
        for i in range(len(A)):
            if A[i] != x:
                B.append(i)

    print("Output: ", end = " ")
    print(*B)


arr_size = int(input().strip())
if valid_input(arr_size, 0) == False:
    quit()
type = input().strip()
if valid_input(type,1) == 0:
    quit()
if valid_input(type, 1) == 1:
    array = list(int(arr) 
    for arr in input().strip().split())[:arr_size]
    condition = input().strip()
    if valid_input(condition, 2) == 0:
        quit()
    x = int(input().strip())
    find_all(array, x, condition)

elif valid_input(type,1) == 2:
    array = list(str(arr) 
    for arr in input().strip().split())[:arr_size]
    condition = input().strip()
    if valid_input(condition, 2) == 0:
        quit()
    x = input().strip()
    find_all(array, x, condition)  
