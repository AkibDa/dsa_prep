class Solution(object):
  def maxIceCream(self, costs, coins):
    if not costs:
      return 0

    max_val = max(costs)
    count = [0] * (max_val + 1)

    for price in costs:
      count[price] += 1

    canbuy = 0

    for price, freq in enumerate(count):
      if freq == 0:
        continue

      if coins < price:
        break

      max_affordable_at_this_price = coins // price
      buy_amount = min(freq, max_affordable_at_this_price)

      canbuy += buy_amount
      coins -= (buy_amount * price)

    return canbuy