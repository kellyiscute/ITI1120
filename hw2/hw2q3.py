import random


def performTest(operation):
    ## complete your work here ##
    correctCounts = 0
    for i in range(10):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        if operation == 0:
            ans = int(input(f'{a} + {b} = '))
            if ans == a + b:
                correctCounts += 1
            else:
                print(f'The correct answer is {a+b}')
        else:
            ans = int(input(f'{a} * {b} = '))
            if ans == a * b:
                correctCounts += 1
            else:
                print(f'The correct answer is {a*b}')
    return correctCounts


print("This software tests you with 10 questions …… ")
operation = int(
    input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))

correctCounts = performTest(operation)

if correctCounts <= 6:
    print("Please ask your teacher for help.")
else:
    print("Congratulations!")
