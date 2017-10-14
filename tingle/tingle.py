#!/usr/bin/python3
import math

N = int(input())
power = math.floor(math.log(N, 2))
print(2*(N-2**power)+1)
