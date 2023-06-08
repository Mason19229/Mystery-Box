import random

balance = int(input("Please enter a starting balance: "))
spins = 0

while balance > 2 and spins < 10:
    balance = balance - 2
    prize_list = [0, 2, 4, 10]
    x = random.choices(prize_list, weights=(75, 10, 10, 5), k=1)
    balance = balance + x[0]
    spins += 1
    print("You got ${}, your total balance is ${} with {} spins".format(x, balance, spins))