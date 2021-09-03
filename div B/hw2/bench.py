def popping_blocks(middle, blocks, k):
    i = 0

    while i < k:
        if blocks[i] < middle < blocks[i] + 1:
            return blocks[i]
        if blocks[i] <= middle <= blocks[i + 1]:
            return "" + str(blocks[i]) + " " + str(blocks[i + 1])
        i += 1


if __name__ == '__main__':
    l, k = list(map(int, input().split()))
    blocks = list(map(int, input().split()))
    middle = l / 2
    print(popping_blocks(middle, blocks, k))
