#!/usr/bin/python3
"""
A script to determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(available_denominations, target_amount):
    """
    A method to determine the fewest number of coins
    needed to meet a given amount total.
    """
    if (target_amount <= 0):
        return (0)
    min_coins_required = [float('inf')] * (target_amount + 1)
    min_coins_required[0] = 0

    for denomination in available_denominations:
        for current_amount in range(denomination, target_amount + 1):
            min_coins_required[current_amount] = min(
                min_coins_required[current_amount],
                min_coins_required[current_amount - denomination] + 1
            )

    if min_coins_required[target_amount] != float('inf'):
        return (min_coins_required[target_amount])
    else:
        return (-1)
