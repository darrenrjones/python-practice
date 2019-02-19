# WARMUP

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    pass

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    pass

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1,n2):
    pass

print(makes_twenty(20,10))
print(makes_twenty(2,3))


#LEVEL 1 PROBLEMS

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    pass

print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    pass

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    pass

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


#LEVEL 2 PROBLEMS

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    pass

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    pass

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    pass

print(blackjack(5,6,7)) #18
print(blackjack(9,9,9)) # 'BUST'
print(blackjack(9,9,11)) # 19

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    pass

print(summer_69([1, 3, 5])) # 9
print(summer_69([4, 5, 6, 7, 8, 9])) # 9
print(summer_69([2, 1, 6, 9, 11])) # 14

#CHALLENGING PROBLEMS:

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


def spy_game(nums):
    pass

print(spy_game([1,2,4,0,0,7,5])) # T
print(spy_game([1,0,2,4,0,5,7])) # T
print(spy_game([1,7,2,0,4,5,0])) # F

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#0 and 1 not primes


def count_primes(num):
    pass

print(count_primes(100)) #25

#JUST FOR FUN

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *

def print_big(letter):
    pass





