#!/usr/bin/python3

INF = 10000000

def sq_euclid_distance(A, B):
    return (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B [2]) ** 2


N, K = [int(val) for val in input().split(" ")]
allowed = []
banned = []
for i in range(N):
    allowed.append(tuple([int(val) for val in input().split(",")]))
for i in range(K):
    banned.append(tuple([int(val) for val in input().split(",")]))

for banned_color in banned:
    best_color = None
    best_distance = INF
    for allowed_color in allowed:
        dist = sq_euclid_distance(banned_color, allowed_color)
        if dist < best_distance:
            best_distance = dist
            best_color = allowed_color
    print(",".join([str(val) for val in best_color]))
