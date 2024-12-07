def parseinput(txt):
    txt = readlines(fn)
    numbers = [int(x) for x in txt[0].split(',')]
    boards = []
    for l in txt[1:]:
        if l == "":
            boards.append(list()) # new board
        else:
            boards[-1].extend([int(x) for x in l.strip().replace('  ', ' ').split(' ')])
    return numbers, boards

def checkboard(board):
    for i in range(0, 5):
        # horz
        if all([board[j] is None for j in range(i*5, i*5+5)]):
            return True
        # vert
        if all([board[k] is None for k in range(i, 25, 5)]):
            return True
    return False

def playbingo(numbers, board):
    for i, n in enumerate(numbers):
        if n in board:
            board[board.index(n)] = None
        if checkboard(board) is True:
            return i, n, board

def part1(results):
    return results[0][1] * sum([x for x in results[0][2] if x is not None])

def part2(results):
    return results[-1][1] * sum([x for x in results[-1][2] if x is not None])

def readlines(fn):
    with open(fn) as f:
        txt = f.read().splitlines()
    return txt

if __name__ == '__main__':
    fn = 'd04.txt'
    # fn = 'd04eg.txt'
    numbers, boards = parseinput(fn)
    results = [playbingo(numbers, board) for board in boards]
    results.sort(key = lambda x: x[0])
    print(part1(results))
    print(part2(results))
