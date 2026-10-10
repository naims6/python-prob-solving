# 10 Easy Python Problems

# 1. Print Your Name
# name = "Naim"
# country = "Bangladesh"
# age = 21
# print(f"Hello, I am {name}. I live in {country}. I am {age} years old.")

# 2. Add Two Numbers

# try: 
#     a = int(input("First Number: "))
#     b = int(input("Second Number "))

#     total = a + b
#     print (f"Total: {total}")
# except ValueError:
#     print("Invalid input! Please enter numbers only, not text.")
    
# 3. Even or Odd

# Take an integer as input and determine whether it is even or odd.
# Example: 8 → Even
# Concept: if-else, modulo operator %

# number = int(input("Give me a Number: "))

# if(number % 2 == 0):
#     print(f"The Number {number} is Even")
# else:
#     print(f"The Number {number} is Odd")

# 4. Find the Largest Number

# Take three numbers as input and print the largest one.
# Example: 10, 25, 15 → 25
# Concept: Conditions and comparisons   

# a = int(input("First Number: "))
# b = int(input("Second Number: "))
# c = int(input("Third Number: "))


# if(a > b and a > c):
#     print(f"{a} is greater then {b} and {c}")
# elif(b > a and b > c):
#     print(f"{b} is greater then {a} and {c}")
# else:
#     print(f"{c} is greater then {a} and {b}")
  
    
# 5. Calculate a Factorial

# Take a non-negative integer and calculate its factorial.
# Example: 5 → 120 because 5!=5×4×3×2×1.
# Concept: Loops and multiplication

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     return factorial(n-1) * n

# resutl = factorial(10)

# print(resutl)

# 6. Print Numbers from 1 to N
# Take a number N and print every integer from 1 to N.
# Example: 5 → 1 2 3 4 5
# Concept: for loops and range()

# number = int(input("Give me a number :"))

# for i in range(number):
#     print(f"{i + 1}")


# 7. Sum of Digits
# Take a positive integer and calculate the sum of its digits.
# Example: 1234 → 10 because 1 + 2 + 3 + 4 = 10.
# Concept: Loops and arithmetic

# def sumOfDigits(n):
#     sum = 0
#     for i in range(len(n)):
#         sum += int(n[i])

#     print("Total", sum)

# sumOfDigits("123456")

# 8. Reverse a String

# Take a string and print it in reverse order.
# Example: python → nohtyp
# Concept: Strings and slicing

# method 1
# def reverseStr(text: str):
#     reversedText = ""
#     for char in text:
#         reversedText = char + reversedText
#     print(reversedText)
    
# method 2
# def reverseStr(text: str):
#     print("".join(reversed(text)))


# reverseStr("python, Javasript")

# 9. Check for a Palindrome
# Determine whether a word reads the same forward and backward.
# Example: madam → Palindrome; hello → Not a palindrome.
# Concept: Strings and conditions

# def checkPalindrome(text: str):
#     reversedText = "".join(reversed(text))
#     if(reversedText == text):
#         print("This is a Palindrome")
#     else:
#         print("this is not palindrome")

# checkPalindrome("hello")
# checkPalindrome("madam")


# 10. FizzBuzz
# Print numbers from 1 to 30. For multiples of 3, print Fizz; for multiples of 5, print Buzz; for multiples of both, print FizzBuzz.
# Example: 3 → Fizz, 5 → Buzz, 15 → FizzBuzz.
# Concept: Loops, conditions, and logical operators

for i in range(30):
    if i % 5 == 0 and i % 3 == 0:
        print(f"This {i} is FizzBuzz")
    elif i % 3 == 0:
        print(f"This {i} is Fizz")
    elif i % 5 == 0:
        print(f"This {i} is Buzz")
