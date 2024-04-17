'''
== Assignment (Programming Fundamentals)
== Department of Software Engineering
== Name: 
== Reg#: 
== Submitted to: 
'''
''' Exercise 1: 
== Calculate the multiplication and sum of two numbers.
Given two integer numbers, return their product only if the product is equal to or lower than
1000. Otherwise, return their sum. '''
print("First Question Started Here")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

product = num1 * num2

if product <= 1000:
    print("Product:", product)
else:
    print("Sum:", num1 + num2)

'''
Exercise 2:
== Print the sum of the current number and the previous number.
'''
print("Second Question Started Here")

prev_number = int(input("Enter previous Number: "))
print(prev_number)
while True:
    current_number = int(input("Enter current Number: "))
    if current_number == 0:
        break
    print(current_number + prev_number)
    prev_number = current_number

'''
Exercise 3:
== Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an
even index number.
For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’
'''
print("Third Question Started Here")

string = input("Enter a string: ")
even_characters = string[::2]
for character in even_characters:
    print(character)

'''
Exercise 4:
== Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new
string.
'''
print("Fourth Question Started Here")
string = input("Enter the string")
n = int(input("Enter the n"))

if n < len(string):
    print(string[n:])
else:
    print("n must be less than the length of the string.")

'''
Exercise 5:
== Check if the first and last number of a list is the same.
Write a program to print “First and Last Numbers are same” if the first and last numbers of a
given list are the same. If the numbers are different then print “Not Same”
'''
print("Fifth Question Started Here")
numbers = input("Enter numbers separated by space: ").split()
first_number = numbers[0]
last_number = numbers[-1]

if first_number == last_number:
    print("First and Last Numbers are same")
else:
    print("Not Same")

'''
Exercise 6:
== Display numbers divisible by 5 from a list.
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''
print("Sixth Question Started Here")

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

for num in numbers:
    if num % 5 == 0:
        print(num)

'''
Exercise 7: Print the following pattern.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
print("Seventh Question Started Here")

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print("Result Done")

'''
Exercise 8:
== Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse. For example, 545, is the
palindrome numbers
'''
print("Eighth Question Started Here")

number = input("Enter a number: ")

if number == number[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")

'''
Exercise 9:
== Create a new list from two list using the following condition
Create a new list from two list using the following condition
Given two list of numbers, write a program to create a new list such that the new list should
contain odd numbers from the first list and even numbers from the second list.
'''
print("Nineth Question Started Here")

list1 = [int(x) for x in input("Enter numbers for the first list separated by space: ").split()]
list2 = [int(x) for x in input("Enter numbers for the second list separated by space: ").split()]

new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

print("New list:", new_list)

'''
Exercise 10:
== Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
digits
'''
print("Tenth Question Started Here")

number = int(input("Enter an integer: "))
digits = []

while number > 0:
    digit = number % 10
    digits.append(digit)
    number //= 10

reversed_digits = reversed(digits)
print(" ".join(map(str, reversed_digits)))
