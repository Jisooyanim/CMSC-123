def array_rotation(array_size, array, k):
    for i in range(0, k):
        last_element = array[array_size - 1]#Stores the last element

        for j in range(array_size - 1, -1, -1):
            array[j] = array[j - 1]
        array[0] = last_element#Makes the last element the first

Array_size = int(input())#size of the array
Array = list(int(i) for i in input().strip().split())[:Array_size]#elements
Rotation = int(input())#k movements
array_rotation(Array_size, Array, Rotation)
print(Array)