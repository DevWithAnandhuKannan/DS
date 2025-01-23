# 1. Sum of Digits (with an accumulator)
# Write a function that calculates the sum of digits of a given number using parameterized recursion. The function should take two parameters: the number and an accumulator that will store the running total of the sum.

# def cal(num,sum):
#          if(num>0):
#                   res = num % 10
#                   sum = sum + res
#                   return cal(num//10,sum)
#          else:
#                  return sum

# num = 123
# print(cal(num,0))


# ----------------------------------------------------------------------------------------------------------------------
# 2. Fibonacci with Memoization
# fib : 0,1,1,2,3,5, .......

# def fib(num, memo={0:1,1:1}):
#          if num in memo:
#                  return memo[num]
#          else:
#                  memo[num] = fib(num-1, memo)+ fib(num-2, memo)
#                  return memo[num]


# num = 4
# print(fib(num))

# ----------------------------------------------------------------------------------------------------------------------
# 3. Find the Greatest Common Divisor (GCD)
# Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36
# Factors of 60: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60

# def gcd(a, b):
#          if a == 0 :
#                   return b
#          if b == 0:
#                   return a
#          # if smaller == None:
#          #          smaller = min(a,b)
#          if a>b :
#                  return gcd(a-b,b)
#          else:
#                  return gcd(a, b-a)
     
# a = 56
# b = 98
# print(gcd(a, b))


# 36,24
# 12,24
# 12,12

# 56,98
# 56,42
# 14,42
# 14,28
# 14,14

# ----------------------------------------------------------------------------------------------------------------------
# 4. Power Function (Exponentiation by Squaring)
# Write a recursive function to compute x^n (x raised to the power of n) using parameterized recursion. The function should use an additional parameter to accumulate the result.

# def cal(x,n,result=1):
#          if(n==0):
#                   return result
         
#          return cal(x,n-1,result*x)

# print(cal(3,4))
# 3,4,
# 3,3,3
# 3,2,9
# 3,1,27
# 3,0,81

# ----------------------------------------------------------------------------------------------------------------------
# 5. Reverse a String
# Write a function to reverse a string using parameterized recursion. The function should take two parameters: the string and an accumulator to build the reversed string.

# def rev_string(String, ans=''):
#          if not String:
#                   return ans
#          return rev_string(String[:-1], ans+String[-1])
# print(rev_string('Anandhu'))

# ----------------------------------------------------------------------------------------------------------------------

# 6. Counting Occurrences of an Element
# Write a function to count how many times a specific element appears in a list using parameterized recursion. The function should take the list and a counter as parameters.

# def occurance(lst, target, count=0):
#          if not lst:
#                  return count
#          return occurance(lst[1:],target,count+(1 if lst[0]== target else 0))
# print(occurance([1,2,3,4,5,6,6],6))

# ----------------------------------------------------------------------------------------------------------------------
# 7. Flatten a Nested List
# Write a function that flattens a nested list (a list that may contain other lists) into a single list using parameterized recursion. The function should take the nested list and an accumulator to hold the flattened elements.

# ls = [1, [2, [3], 4], [5, 6, [7, [8, 9, [10]]]]]

# def flattern(nestedls, res = None):
#          if res == None:
#                  res = []
#          for i in nestedls:
#                   if isinstance(i,list):
#                            flattern(i,res)
#                   else:
#                            res.append(i)
#          return res
# print(flattern(ls))


# ----------------------------------------------------------------------------------------------------------------------
# 8. Path Sum in a Binary Tree
# Given a binary tree, write a function to find if there is a path from the root to a leaf such that the sum of the values along the path equals a target sum. Use parameterized recursion where you pass the current sum along with the recursion.
