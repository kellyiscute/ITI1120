amount_owed = float(input('Enter the amount you are owed in $: '))
coins = 0
coins += int(amount_owed // 0.25)
amount_owed %= 0.25

coins += amount_owed // 0.10
amount_owed %= 0.10

coins += amount_owed // 0.05
amount_owed %= 0.05

coins += amount_owed // 0.01

print('The minimum number of coins the cashier can return is:', int(coins))
