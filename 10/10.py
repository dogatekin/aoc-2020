import fileinput

ratings = list(map(int, fileinput.input()))

ratings.sort()

diffs = [ratings[0]]
for i in range(1, len(ratings)):
    diffs.append(ratings[i] - ratings[i-1])
diffs.append(3)

print(diffs.count(1) * diffs.count(3))

r = [0] + ratings + [ratings[-1]+3]
dp = [0]*len(r)
dp[-1] = 1

for i in range(len(r)-1, -1, -1):
    for j in range(i+1, len(r)):
        if r[j] <= r[i] + 3:
            dp[i] += dp[j]
        else:
            break

print(dp[0])
