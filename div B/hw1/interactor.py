def make_a_result(interactor, checker, code):
    if interactor in (2, 3, 5):
        return interactor
    elif interactor == 0:
        if code == 0:
            return checker
        return 3
    elif interactor == 1:
        return checker
    elif interactor == 4:
        if code == 0:
            return 4
        return 3
    elif interactor == 6:
        return 0
    elif interactor == 7:
        return 1
    else:
        return interactor


if __name__ == '__main__':
    code = int(input())
    interactor = int(input())
    checker = int(input())

    print(make_a_result(interactor, checker, code))
