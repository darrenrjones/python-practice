# Write a function that computes the volume of a sphere given its radius.

import string
import math


def vol(rad):
    return 4/3 * math.pi * rad**3

# print(vol(3))

# Write a function that checks whether a number is in a given range(Inclusive of high and low)


def ran_check(num, low, high):
    return num in range(low, high+1)

# print(ran_check(5,1,5))


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    upperCount = 0
    lowerCount = 0
    for char in s:
        if char.isupper():
            upperCount += 1
        elif char.islower():
            lowerCount += 1
        else:
            pass

    # print(f"No. of Upper case characters : {upperCount}")
    # print(f"No. of Lower case characters : {lowerCount}")


# print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def unique_list(l):
#     return list(set(l))

def unique_list(l):
    unique = []
    for n in l:
        if n not in unique:
            unique.append(n)
    return unique

# print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))  # [1, 2, 3, 4, 5]


# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    total = 1
    for n in numbers:
        total *= n
    return total


# print(multiply([1, 2, 3, -4]))  # -24


# Write a Python function that checks whether a passed string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


# print(palindrome('helleh'))  # True
# print(palindrome('staples'))  # False
# print(palindrome('a man a plan a canal panama'))  # True


# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Hint: Look at the string module


def ispangram(str1, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(str1.lower())
     


print(ispangram("The quick brown fox jumps over the lazy dog")) # True
# string.ascii_lowercase 
# # 'abcdefghijklmnopqrstuvwxyz'
