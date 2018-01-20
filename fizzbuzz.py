
b = int(input('Insert number between 1 and 100: '))
if b > 100:
    print('Your number was to high. Default value set at 100')
    b = 100
for i in range(1,b):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
