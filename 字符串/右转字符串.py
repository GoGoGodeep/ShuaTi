import sys

n = int(sys.stdin.readline())
chars = sys.stdin.readline()

n %= len(chars)

result = chars[-n:] + chars[:-n]

print(result)
