#한번의 거래로 낼 수 있는 최대 이익을 산출하라.

prices: list[int] = [7, 1, 5 ,3 ,6, 4]
max_price: int = 0

for i, price in enumerate(prices):
  for j in range(i, len(prices)):
    max_price = max(prices[j] - price, max_price)

print(max_price)