def FizzBuzz(bounds, triggers):
    for i in range(bounds[0], bounds[1]):
        result = ''
        for pair in triggers:
            if pair[1](i):
                result += pair[0]

        print(result) if result != '' else print(i) 



FizzBuzz(
    (1, 110), 
    (
        ('Fizz', lambda i: i % 3 == 0), 
        ('Buzz', lambda i: i % 5 == 0), 
        ('Zap', lambda i: i < 10))
    )