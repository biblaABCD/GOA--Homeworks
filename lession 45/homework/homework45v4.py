def separate_even_odd():
    even_numbers = []
    odd_numbers = []

    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    print(even_numbers, odd_numbers)

separate_even_odd()