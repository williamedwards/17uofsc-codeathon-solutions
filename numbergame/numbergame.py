#!/usr/bin/python3

BUELL = 0
FENNER = 1
def print_guy(turn):
    if turn == BUELL:
        print("BUELL")
    else:
        print("FENNER")

def update_cached(cached, values, turn_mask):
    for value in reversed(values):
        cached[value] = turn_mask
        turn_mask ^= 1

T = int(input())
Ns = []
for i in range(T):
    Ns.append(int(input()))

cached = {}

for N in Ns:
    turn = BUELL
    values = []
    while True:
        if N in cached:
            print_guy(cached[N] ^ turn)
            break
        values.append(N)
        # Compute <= power of 2
        temp = N
        p = 0
        while temp > 1:
            temp = temp >> 1
            p += 1
        next_lowest_pow = 1 << p
        if N == next_lowest_pow:
            if p % 2 == 1:
                update_cached(cached, values, 0)
                print_guy(turn)
            else:
                turn ^= 1
                update_cached(cached, values, 1)
                print_guy(turn)
            break
        else:
            N -= next_lowest_pow
        turn ^= 1
