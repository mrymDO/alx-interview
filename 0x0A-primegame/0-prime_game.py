#!/usr/bin/python3
"""
Prime game
"""


def generate_primes(limit):
    """Generate a list of primes"""
    primes = []
    is_prime = [True] * (limit + 1)

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes


def isWinner(x, nums):
    """Determine the winner"""
    if x is None or nums is None or x == 0 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    for limit in nums:
        primes = generate_primes(limit)
        winner = 'Ben' if len(primes) % 2 == 0 else 'Maria'
        ben_wins += (winner == 'Ben')
        maria_wins += (winner == 'Maria')

    return 'Maria' if maria_wins > ben_wins \
        else 'Ben' if ben_wins > maria_wins else None
