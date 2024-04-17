'''
== Assignment (Programming Fundamentals)
== Department of Software Engineering
== Name: 
== Reg#: 
== Submitted to: 
'''
''' Exercise 1: 
 '''


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

product = num1 * num2

if product <= 1000:
    print("Product:", product)
else:
    print("Sum:", num1 + num2)

'''
Exercise 2:
'''


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
'''


string = input("Enter a string: ")
even_characters = string[::2]
for character in even_characters:
    print(character)

'''
Exercise 4:

'''

string = input("Enter the string")
n = int(input("Enter the n"))

if n < len(string):
    print(string[n:])
else:
    print("n must be less than the length of the string.")

'''
Exercise 5:

'''

numbers = input("Enter numbers separated by space: ").split()
first_number = numbers[0]
last_number = numbers[-1]

if first_number == last_number:
    print("First and Last Numbers are same")
else:
    print("Not Same")

'''
Exercise 6:

'''


numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

for num in numbers:
    if num % 5 == 0:
        print(num)

'''
Exercise 7:
'''


rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print("Result Done")

'''
Exercise 8:

'''


number = input("Enter a number: ")

if number == number[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")

'''
Exercise 9:

'''


list1 = [int(x) for x in input("Enter numbers for the first list separated by space: ").split()]
list2 = [int(x) for x in input("Enter numbers for the second list separated by space: ").split()]

new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

print("New list:", new_list)

'''
Exercise 10:

'''

number = int(input("Enter an integer: "))
digits = []

while number > 0:
    digit = number % 10
    digits.append(digit)
    number //= 10

reversed_digits = reversed(digits)
print(" ".join(map(str, reversed_digits)))
