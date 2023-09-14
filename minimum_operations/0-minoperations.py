#!/usr/bin/python3

def minOperations(n):
    '''Calculates the fewewst number of operations neede to result in exactly n H characters in the file.
    Returns:
      integer: if n is impossible to achieve, return 0'''

    chars_pasted = 1
    copied = 0
    counter = 0


    while chars_pasted < n:
        #while above and if nothing in copied
        if copied ==0:
            #copy
            copied = chars_pasted
            counter += 1


        #while above and if nothing pasted
        if chars_pasted == 1:
            #paste
            pasted_chars += copied
            counter += 1
            continue


        remaining = n - chars_pasted
        if remaining % chars_pasted !=0:
            #paste current clipboard
            chars_pasted += copied
            counter += 1

        else:
            #copy all
            copied = chars_pasted
            chars_pasted += copied
            counter += 2


        if char_pasted == n:
            return counter
        else:
            return 0


