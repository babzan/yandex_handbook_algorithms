def HanoiTower(n, fromPeg, toPeg):
    if n == 1:
        # print(f"{fromPeg} {toPeg}")
        newArr.append([fromPeg, toPeg])
        return
    unusedPeg = 6 - fromPeg - toPeg
    HanoiTower(n-1, fromPeg, unusedPeg)
    # print(f"{fromPeg} {toPeg}")
    newArr.append([fromPeg, toPeg])
    HanoiTower(n-1, unusedPeg, toPeg)

fromPeg = 1
toPeg = 3
n = int(input())
newArr = []
HanoiTower(n, fromPeg, toPeg)
print(len(newArr))
for i in range(len(newArr)):
    print(*newArr[i])
