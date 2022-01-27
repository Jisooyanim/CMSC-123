def create_stack():
    stack = []
    return stack

def push(stack, element):
    stack.append(element)

def pop(stack):
    if len(stack) == 0:
        return
    else:
        stack.pop()

def maximum(stack, arr):
    if len(stack) == 0:
        arr.append(-100)
    else: 
        largest_number = max(stack)
        arr.append(largest_number)

def print_array(arr):
    print("Output: ")
    for i in range(0, len(arr)):
        print(arr[i], end = '\n')


n = int(input("Input: "))
stack = create_stack()
arr = []
while n != 0:
    operation = input().split()
    if operation[0] == "push":
        element = operation[1]
        push(stack, element)
    elif operation[0] == "pop":
        pop(stack)
    elif operation[0] == "max":
        maximum(stack, arr)
    n -= 1
print_array(arr)