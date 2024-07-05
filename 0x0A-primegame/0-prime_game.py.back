#!/usr/bin/python3
"""
Prime Game Module
"""

def isWinner(x, nums):
    """
    A methid to determine the winner.
    """
    num_rounds = x
    numbers = nums
    if num_rounds < 1 or not numbers:
        return None

    maria_wins, ben_wins = 0, 0
    max_num = max(numbers)
    primes = [True] * (max_num + 1)
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, max_num + 1, i):
            primes[j] = False
    for _, num in zip(range(num_rounds), numbers):
        primes_count = sum(1 for x in primes[:num] if x)
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
