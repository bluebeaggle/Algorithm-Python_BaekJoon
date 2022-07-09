import sys

a = [int(sys.stdin.readline()) for i in range(10)]
b = set(map(lambda x: x%42, a))
print(len(b))