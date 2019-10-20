def print_num_while(n):
    c = 1
    while c <= n:
        print(c)
        c += 1


def print_num_for(n):
    for i in range(1, n + 1):
        print(i)


n = input('Enter the number N: ')
print_num_for(n)
print_num_while(n)
