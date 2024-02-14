def find_maximum(numbers, comparison_function):
    if not numbers:
        return None
    
    max_number = numbers[0]
    for num in numbers[1:]:
        if comparison_function(num, max_number) > 0:
            max_number = num
    return max_number


numbers = [5, 2, 8, 1, 9, 3]
max_num = find_maximum(numbers, lambda x, y: x - y)  # Using lambda function to compare two numbers
print("Maximum number:", max_num)
