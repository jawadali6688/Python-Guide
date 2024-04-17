num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

sum = num1 + num2
product = num1 * num2

if product <= 1000:
    print("The answer is Less or Equal to 1000 that's why I have returned the Product ", product)

else:
    print("The answer is greater than 1000 that's why I have returned the Sum ", sum)