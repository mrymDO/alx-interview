#!/usr/bin/python3
""" making change module
"""


def makeChange(coins, total):
    """number of coins needed to  meet the total
    """
    if total <= 0:
        return 0

    if len(coins) is 0:
        return -1

    coins = sorted(coins)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
