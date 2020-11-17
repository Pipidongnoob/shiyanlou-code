#!/usr/bin/env python3
N = 10
sum = 0
count = 0
while count < N:
    number = float(input())
    sum += number
    count += 1
average = sum / N
print('N = %d Sum = %.2f' % (N, sum))
print('Average = %.2f' % average)

