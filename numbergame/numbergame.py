#!/usr/bin/python3

BUELL = 0
FENNER = 1
def print_guy(turn):
    if turn == BUELL:
        print("BUELL")
    else:
        print("FENNER")

T = int(input())
Ns = []
for i in range(T):
    Ns.append(int(input()))

# Super Naive Version
for N in Ns:
    turn = BUELL
    while True:
        # Compute <= power of 2
        temp = N
        p = 0
        while temp > 1:
            temp = temp >> 1
            p += 1
        next_lowest_pow = 1 << p
        if N == next_lowest_pow:
            if p % 2 == 1:
                print_guy(turn)
            else:
                turn ^= 1
                print_guy(turn)
            break
        else:
            N -= next_lowest_pow
        turn ^= 1
