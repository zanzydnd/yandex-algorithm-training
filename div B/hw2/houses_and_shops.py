buildings = list(map(int, input().split()))

# 1 - жилой
# 2 - магазин
shops = set()
for i in range(len(buildings)):
    if buildings[i] == 2:
        shops.add(i)

