# Parameterized FizzBuzz. User can input terms that are not Fizz or Buzz for parsing.

def FizzBuzz(bounds, triggers):
    for i in range(bounds[0], bounds[1]):
        result = ''
        for pair in triggers:
            if i % pair[1] == 0:
                result += pair[0]

        print(result) if result != '' else print(i) 



FizzBuzz(
    (1, 110), 
    (
        ('Fizz', 3), 
        ('Buzz', 5), 
        ('Zap', 7))
    )
