#!/usr/bin/python3
'''Minimum Operations python3 ALX challenge'''


def minOperations(n):
    '''calculates fewest number of
    operations needed to result in exactly n H
    characters.
    Returns:
        Integer - if n is impossible to achieve then return 0
    '''
    pasted_chars = 1 
    clipboard = 0 
    counter = 0 

    while pasted_chars < n:
        # if it didn;t copy anything
        if clipboard == 0:
            # it copied all
            clipboard = pasted_chars
            # increment the operations counter
            counter += 1

        # if have not pasted anything
        if pasted_chars == 1:
            # paste something
            pasted_chars += clipboard
            # increment the operations counter
            counter += 1
            # continue to the next loop
            continue

        remaining = n - pasted_chars 
        # check if it impossible by checking if clipboard
        # has more than needed to reach number desired
        # meaning num of chars in file is equal
        # or more than in clipboard.
        # in both it is impossible to get n of chars
        if remaining < clipboard:
            return 0

        # if it can not be devided
        if remaining % pasted_chars != 0:
            # paste the current clipboard
            pasted_chars += clipboard
            # increment the operations counter
            counter += 1
        else:
            # it copied yall
            clipboard = pasted_chars
            # paste something
            pasted_chars += clipboard
            # increment the operations counter
            counter += 2

    # if got desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
