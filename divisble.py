#!/usr/bin/env python

# List all the possible divisors for given number
natNum = int(input("Give an integer: "))

for i in range(1, natNum + 1):
    if natNum % i == 0:
        print(i)
