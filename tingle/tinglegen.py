#!/usr/bin/python3
def tingle(N):
    bros = list(range(1, N+1))
    curr = 1
    while len(bros) > 1:
        del bros[curr]
        curr = (curr + 1) % len(bros)
    print(bros)
for i in range(2, 100):
    print("{}: ".format(i), end="")
    tingle(i)
