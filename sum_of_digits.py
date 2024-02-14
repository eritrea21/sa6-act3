#lambda function to calculate the sum of the digits
sum_of_digits = lambda n: sum(int(digit) for digit in str(n) if digit.isdigit())

# input a number from a user
number = int(input("Enter a number: "))

# Calculate the sum of digits using the lambda function
result = sum_of_digits(number)

# print the result
print("Sum of digits: " , result)