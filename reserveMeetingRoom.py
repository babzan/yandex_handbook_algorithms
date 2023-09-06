def find_max_non_overlapping_intervals(n, intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_interval_end = -1

    for interval in intervals:
        if interval[0] > prev_interval_end:
            count += 1
            prev_interval_end = interval[1]
    return count

n = int(input())
intervals = []
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

result = find_max_non_overlapping_intervals(n, intervals)
print(result)
