def solve_equation(a, b, c, d):
    if b == 0 and a != 0:
        return "NO"
    if b == 0 and a == 0:
        return "INF"
    x = b / a * -1
    if c * x + d == 0:
        return "NO"
    if x - int(x) == 0:
        return int(x)
    return "NO"

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(solve_equation(a, b, c, d))
