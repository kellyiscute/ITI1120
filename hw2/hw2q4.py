import random


def doTest(operation):
    ## complete your work here ##
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    if operation == 0:
        ans = int(input(f'{a} + {b} = '))
        if ans == a + b:
            return True
        else:
            print(f'The correct answer is {a+b}')
            return False
    else:
        ans = int(input(f'{a} * {b} = '))
        if ans == a * b:
            return True
        else:
            print(f'The correct answer is {a*b}')
            return False


responsesCorrect = 0
print("The software will process a test with 10 questions …… ")
for compteur in range(10):
    operation = random.randint(0, 1)
    if doTest(operation) == True:
        responsesCorrect += 1
print(responsesCorrect, "Correct responses")
if responsesCorrect <= 6:
    print("Ask some help from your instructor.")
else:
    print("Congratulations!")
