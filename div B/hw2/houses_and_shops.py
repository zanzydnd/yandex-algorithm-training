buildings = list(map(int, input().split()))

# 1 - жилой
# 2 - магазин
local_min = 0
maximum = 0
for i in range(len(buildings)):
    left = 10
    right = 10
    if buildings[i] == 1:
        for m in reversed(range(0, i)):
            if buildings[m] == 2:
                left = i - m
                break
        for l in range(i, 10):
            if buildings[l] == 2:
                right = l - i
                break
        local_min = min(right, left)
        # print("right: ", right, "left:", left)
        # print("house n: ", i, "shortest distance: ", local_min)
    maximum = max(local_min, maximum)

print(maximum)
