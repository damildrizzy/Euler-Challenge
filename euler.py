"""
Question 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
#Solution 1:
values = []
i = 3
while i < 1000:
    if (i % 5 == 0) | (i % 3 == 0):
        values.append(i)
    i += 1
    
print(sum(values))

#Answer = 233168

