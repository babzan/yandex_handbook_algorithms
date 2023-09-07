stones = [int(x) for x in input().split()]

n = stones[0]
m = stones[1]

if (n % 2 == 0 and m % 2 == 0):
    print("Loose")
else:
    print("Win")
