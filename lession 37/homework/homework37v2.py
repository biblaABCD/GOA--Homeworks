def number():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80 ,90]
    numbers.append(100)
    numbers.insert(0, 5)
    numbers.remove(30)
    numbers.sort()
    numbers.reverse()
    print(numbers, numbers.count(20), numbers.index(50))

number()