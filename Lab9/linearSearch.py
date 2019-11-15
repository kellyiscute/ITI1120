import random


def find(l, c):
    for i in range(l.__len__()):
        if l[i] == c:
            print(f'Number of steps: {i+1}')
            print(True)
            return
    print(f'Number of steps: {l.__len__()}')
    print(False)


if __name__ == "__main__":
    l = []
    for i in range(random.randint(100, 10000)):
        l.append(random.randint(100, 1000))
    find(l, random.randint(100, 1000))
