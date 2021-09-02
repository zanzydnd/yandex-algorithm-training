string = input()

if len(string) % 2 == 0:
    first_half_begining = 0
    first_half_end = len(string) // 2 - 1
    second_half_begining = len(string) // 2
    second_half_ending = len(string) - 1
    first_half = string[first_half_begining:first_half_end + 1]
    second_half = string[second_half_begining:second_half_ending + 1]
    i = 0
    j = len(second_half) - 1
    count = 0
    while i < len(first_half):
        if first_half[i] != second_half[j]:
            count += 1
        i += 1
        j -= 1
else:
    middle = len(string) // 2
    first_half = string[:middle]
    second_half = string[middle:]
    i = 0
    j = len(second_half) - 1
    count = 0
    while i < len(first_half):
        if first_half[i] != second_half[j]:
            count += 1
        i += 1
        j -= 1

print(count)
