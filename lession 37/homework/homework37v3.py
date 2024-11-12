def numbr():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_half = numbers[0:5]
    other_half = numbers[4:10]
    squares = [num ** 2 for num in numbers]
    print(numbers, first_half, other_half, squares)


numbr()
    