# coding: utf-8

problem = """
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

coins = [1,2,5,10,20,50,100,200]
m = num_ways_by_amount_and_max_coin = {}
for coin in coins:
    m[0, coin] = 1
for amount in range(1,201):
    for i, max_coin in enumerate(coins):
        m[amount, max_coin] = sum([m[amount - coin, coin] for coin in coins[:i+1] if amount - coin >= 0])
print num_ways_by_amount_and_max_coin[200,200]
