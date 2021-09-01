def is_point_in_triangle(d, x, y):
    if x <= d and x >= 0 and y <= d and y >= 0 and not (x == d and y == d):
        return 0
    else:
        dist_to_a = (x ** 2 + y ** 2) ** (1 / 2)  # 1
        dist_to_b = ((x - d) ** 2 + y ** 2) ** (1 / 2)  # 2
        dist_to_c = ((y - d) ** 2 + x ** 2) ** (1 / 2)  # 3

        min = dist_to_c
        answer = 3

        if dist_to_b <= min:
            answer = 2
            min = dist_to_b
        if dist_to_a <= min:
            answer = 1

        return answer


if __name__ == '__main__':
    d = int(input())
    x, y = list(map(int, input().split()))
    print(is_point_in_triangle(d, x, y))
