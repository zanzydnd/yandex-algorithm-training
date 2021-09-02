n = int(input())

folders = list(map(int, input().split()))

local_max = 0
sum = 0
for folder in folders:
    if folder > local_max:
        sum += local_max
        local_max = folder
    else:
        sum += folder
print(sum)
