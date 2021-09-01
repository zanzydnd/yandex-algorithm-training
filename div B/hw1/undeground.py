n, i, j = input().split(" ")

default = abs(int(i) - int(j)) - 1

if int(i) < int(j):
    through_last_station = (int(i) - 1) + (int(n) - int(j))
else:
    through_last_station = (int(n) - int(i)) + (int(j) - 1)

print(default if default < through_last_station else through_last_station)
