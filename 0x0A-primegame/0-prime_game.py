#!/usr/bin/python3
"""Prime Game
"""


def isWinner(x, nums):
    """Prime game winner"""

    def is_prime(num):
        """check if a number is a prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    memo_primes = {}

    def get_primes_up_to_n(n):
        """get list of prime numbers up to n"""
        if n not in memo_primes:
            primes = [i for i in range(2, n + 1) if is_prime(i)]
            memo_primes[n] = primes
        return memo_primes[n]

    def optimal_moves(nums):
        """find optimal moves"""
        primes = get_primes_up_to_n(max(nums))
        for prime in primes:
            if prime in nums:
                return [num for num in nums if num % prime != 0]

    maria_wins = 0
    ben_wins = 0

    for round_num in range(x):
        current_round = nums[round_num]
        current_nums = list(range(1, current_round + 1))

        while current_nums:
            current_nums = optimal_moves(current_nums)
            if not current_nums:
                ben_wins += 1
                break

            current_nums = optimal_moves(current_nums)
            if not current_nums:
                maria_wins += 1
                break

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
