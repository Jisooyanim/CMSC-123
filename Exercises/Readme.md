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
