max = 0
result = 0
while True:
    number = int(input())
    if number == 0:
        break
    if number > max:
        max = number
        result = 1
    elif number == max:
        result += 1

print(result)