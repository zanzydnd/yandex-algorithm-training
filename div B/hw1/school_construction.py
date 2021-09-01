n = int(input())
students = list(map(int, input().split(" ")))

middle_of_list = int(n / 2 + 0.5) - 1

print(students[middle_of_list])
