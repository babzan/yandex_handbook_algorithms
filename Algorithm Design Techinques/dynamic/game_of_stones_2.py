def canWinStones(n, m):
    memo = {}

    def dp(n, m):
        if n == 0 and m == 0:
            return False
        if (n, m) in memo:
            return memo[(n, m)]

        result = False

        if n >= 1 and not dp(n - 1, m):
            result = True

        if m >= 2 and not dp(n, m - 2):
            result = True

        if n >= 1 and m >= 2 and not dp(n - 1, m - 2):
            result = True

        memo[(n, m)] = result
        return result
    return dp(n, m)

stones = [int(x) for x in input().split()]

n = stones[0]
m = stones[1]

if (canWinStones(n, m)):
    print("Win")
else:
    print("Loose")
