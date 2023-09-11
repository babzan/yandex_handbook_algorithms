n = int(input())
coeff_a = list(map(int, input().split()))
m = int(input())
coeff_b = list(map(int, input().split()))

k = max(n, m)

coeff_c = [0] * (k + 1)

for i in range(n + 1):
    coeff_c[i] += coeff_a[i]
for i in range(m + 1):
    coeff_c[i] += coeff_b[i]

print(k)
print(*coeff_c)
