import sys

prices: list[int] = [7, 1, 5 ,3 ,6, 4]
profit: int = 0
min_price: int = sys.maxsize

prices = [2, 9, 1, 4]

for price in prices:
  min_price = min(min_price, price)
  profit = max(profit, price - min_price)

print(profit)
