"""
Question 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
#Solution 1:
i = 3
while i < 10:
    if (i % 5 == 0) | (i % 3 == 0):
        print(i)
    i += 1