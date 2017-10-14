#!/usr/bin/python3

BUELL = 0
FENNER = 1

T = int(input())
Ns = []
for i in range(T):
    Ns.append(int(input()))

# Super Naive Version
for N in Ns:
    turn = BUELL
    while N > 1:
        # Compute <= power of 2
        temp = N
        p = 0
        while temp > 1:
            temp = temp >> 1
            p += 1
        next_lowest_pow = 1 << p
        if N == next_lowest_pow:
            N = N >> 1
        else:
            N -= next_lowest_pow
        turn ^= 1
    turn ^= 1 # Flip turn back for clarity
    if turn == BUELL:
        print("BUELL")
    else:
        print("FENNER")
