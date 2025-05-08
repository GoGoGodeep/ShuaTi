# https://kamacoder.com/problempage.php?pid=1046

M, N = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(M):
    weight = weights[i]
    value = values[i]
    for j in range(N, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[N])
