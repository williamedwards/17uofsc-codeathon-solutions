#!/usr/bin/python3

T = int(input())
Ns = []
for i in range(T):
    Ns.append(int(input()))


for N in Ns:
    # Count ones and locate rightmost
    num_ones = 0
    pos_rightmost_one = -1
    i = 0
    while N > 0:
        if N & 1 == 1:
            num_ones += 1
            if pos_rightmost_one == -1:
                pos_rightmost_one = i
        i += 1
        N >>= 1
    if (pos_rightmost_one + num_ones) % 2 == 0:
        print("BUELL")
    else:
        print("FENNER")
