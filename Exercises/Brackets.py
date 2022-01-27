def if_balanced(user_input) :
    opening_brackets = ['{', '[', '(']
    closing_brackets = ['}', ']', ')']
    arr = []
    balanced = 1 
    index = 0
    for letter in range(0, len(user_input)):
        index += 1
        if user_input[letter] in opening_brackets:
            arr.append(user_input[letter])
        elif user_input[letter] in closing_brackets:
            i = closing_brackets.index(user_input[letter])
            if ((len(arr) > 0) and (opening_brackets[i] == arr[len(arr)-1])):
                arr.pop()
            else:
                balanced = 0
                break
    if len(arr) == 0 and balanced == 1:
        print("Success")
    else:
        print(str(index))

user_input = input().strip()
if_balanced(user_input)