import sys

sys.setrecursionlimit(100000)


def find(u):
    if gates[u] == u:
        return u
    gates[u] = find(gates[u])
    return gates[u]


def docking(u):
    u = find(u)
    if u == 0:
        return False

    gates[u] = u - 1
    return True


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

gates = [i for i in range(G + 1)]
arrived = 0

for _ in range(P):
    plain_num = int(sys.stdin.readline())
    if not docking(plain_num):
        break
    arrived += 1
print(arrived)