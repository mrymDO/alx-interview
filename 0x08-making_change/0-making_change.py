#!/usr/bin/python3
""" making change module
"""


def makeChange(coins, total):
    """number of coins needed to  meet the total
    """
    if (total <= 0):
        return 0
    if len(coins) == 0:
        return -1
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
