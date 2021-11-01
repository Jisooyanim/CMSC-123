## `IterativeFib.java`
Implement a program that computes for the Nth Fibonacci number. The implementation must be iterative (not recursive or closed-form). 

**Program Parameters:**
Input range: 0 <= N <= 100000

### Test Case 1
```
Input: 20
Output: 6765
```
### Test Case 2
```
Input: 7
Output: 13
```

-------------------------
## `PrimeNumbers.java`
Implement a program that lists all prime numbers up to a given N (inclusive). 

**Program Parameters:**

### Test Case 1
```
Input: 20
Output: 2 3 5 7 11 13 17 19
```
### Test Case 2
```
Input: 50
Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

------------------
## `Array_rotate.py`
Given an array of integers N integers, rotate the elements of the array in a clockwise direction in K steps. In other words, elements will be shifted to the right and the last element will move to the beginning of the array. For example, let an array A = [8, 1, 7, 2, 3] consist of N = 5 elements. Suppose we rotate the array in K = 3 steps. The resulting rotated array A' is then A' = [7, 2, 3, 8, 1]. The series of computations is as follows:

     K=0:  A' = [8, 1, 7, 2, 3]

     K=1:  A' = [3, 8, 1, 7, 2]

     K=2:  A' = [2, 3, 8, 1, 7]

     K=3:  A' = [7, 2, 3, 8, 1]

Write an algorithm that solves the computational problem stated above. Implement your solution using Java or Python. You are provided with a starter file (in Java) that handles user inputs. For Java users, the starter file is named "ArrayRotate.java" 

Note that the input and output of your program must be in the following format:

========================================================
```
Input:

5                                  

8 1 7 2 3                          

3                                  


Output:

[7,2,8,3,1]

```
========================================================

You may use the test cases below to evaluate your solution:

**Test case 1:**
```
Input:

5

1 2 3 4 5

3

Output:

[3, 4, 5, 1, 2]
```
**Test case 2:**
```
Input:

4

1 7 3 1

7

Output:

[7, 3, 1, 1]
```

-------------------
## `Find_all.py`
Implement the FindAll(A, x, condition)method in your List class so that it returns a list containing the indices of all elements in an array A that satisfies the condition  given the target value x. For example, let A = [3, 1, 2, 4, 3, 6] be a zero-indexed list. Then, FindAll(A, 3, ‘==’) returns B = [0, 4]. The method must be able to use the following conditions for a List of numeric types:

1. Equal: “==”

2. Greater than: ">"

3. Less than: "<"

4. Greater than or equal: ">="

5. Less than or equal: "<="

6. Not equal: "!="

 If A is a list of Strings, then only condition 1 and 6 will apply. The empty string will be returned if no element satisfies a given condition (as in test case#4). In this exercise, we will only assume two data types  for the list elements – (i) Integer type, and (ii) String type, for brevity.



**Test case #1:** (Command Line/Terminal Format as in Lab Exercise 1)
```
Input: 6                 Expected number of elements in the list

       Numeric           Type of list elements

       3 1 2 4 3 6       The input list must be formatted like this

       ==                The condition must be formatted like this

       3                 This is the target value

 Output: 0 4
```
**Test case #2:**
```
Input: 6

            String

            Hello ABC World Happy World Auto

            !=

            World

 Output:  0 1 3 5
```
 
**Test case #3:**
```
Input: 6

           Numeric

           3 1 2 4 3 6

           <

           4

 Output: 0 1 2 4
```
**Test case #4:**
```
Input: 6

           Numeric

           3 1 2 4 3 6

           >=

           7

Output:
```
-------------------------------

## `Remove_all.py`

Implement the RemoveAll(A, x, condition)method in your List class so that it removes all elements in the array A that satisfies the condition  given the target value x. For example, let A = [3, 1, 2, 4, 3, 6] be a zero-indexed list. Then, RemoveAll (A, 3, ‘==’) returns A' = [1, 2, 4, 6]. The method must be able to use the following conditions for a List of numeric types: 

1. Equal: “==”

2. Greater than: “>”

3. Less than: “<”

4. Greater than or equal: “>=”

5. Less than or equal: “<=”

6. Not equal: “!=”

 

If A is a list of Strings, then only condition 1 and 6 will apply. In this exercise, we will only assume two data types  for the list elements – (i) Integer type, and (ii) String type, for brevity.

**Test case #1:**
```
Input: 6                 Expected number of elements in the list

       Numeric           Expected Type of elements

       3 1 2 4 3 6       The input list must be formatted like this

       ==                The condition must be formatted like this

       3                This is the target value 

Output: 1 2 4 6
```
**Test case #2:**
```
Input: 7

       Numeric

       1 7 2 1 6 7 2

       >

       3

 

Output: 1 2 1 2
```
**Test case #3:** 
```
Input: 7

       Numeric

       1 7 2 1 6 7 2

       ==

       2

 

Output: 1 7 1 6 7
```
**Test case #4:**
```
Input: 7

       Numeric

       1 7 2 1 6 7 2

       ==

       5

Output: 1 7 2 1 6 7 2
```
