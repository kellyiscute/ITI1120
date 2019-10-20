import random


def guess():
    num = random.randint(1, 10)
    tries = 0
    while True:
        g = int(input('Make your guess: '))
        tries += 1
        if g > num:
            print('Too big')
        elif g < num:
            print('Too small')
        else:
            print(f'You win! You have tried {tries} times')
            break


guess()
