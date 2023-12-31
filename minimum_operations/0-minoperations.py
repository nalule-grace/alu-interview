#!/usr/bin/python3
'''minimum operations python3'''


def minOperations(n):
    '''Calculates the fewewst number of operations needed
    to result in exactly n H characters in the file.
    Returns:
      integer: if n is impossible to achieve, return 0'''

    chars_pasted = 1
    copied = 0
    counter = 0

    while chars_pasted < n:
        if copied == 0:
            copied = chars_pasted
            counter += 1

        if chars_pasted == 1:
            chars_pasted += copied
            counter += 1
            continue

        remaining = n - chars_pasted
        if remaining % chars_pasted != 0:
            chars_pasted += copied
            counter += 1

        else:
            copied = chars_pasted
            chars_pasted += copied
            counter += 2

    if chars_pasted == n:
        return counter
    else:
        return 0
