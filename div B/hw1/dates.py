def check_is_date_correct(first, second, year):
    if (second > 12 or first > 12) or (first == second):
        return 1
    else:
        return 0


if __name__ == '__main__':
    first, second, year = input().split(" ")
    print(check_is_date_correct(int(first), int(second), int(year)))
