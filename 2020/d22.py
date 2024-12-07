import timeit

def parse_decks(infile):
    with open(infile) as f:
        txt = f.read().split('\n\n')
    return [[int(x) for x in t.splitlines()[1:]] for t in txt]

def get_score(cards):
    total = len(cards)
    score = sum(c * (total-i) for i, c in enumerate(cards))
    return score

def play_game(p1, p2):
    while True:
        # win conditions
        if len(p1) == 0:
            winner = 2
            cards = p2
            break
        if len(p2) == 0:
            winner = 1
            cards = p1
            break
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    return (winner, cards)

def part1():
    infile = 'day22eg.txt'
    infile = 'day22.txt'
    p1, p2 = parse_decks(infile)
    winner, cards = play_game(p1, p2)
    score = get_score(cards)
    return score

start_time = timeit.default_timer()
print(part1())
print('Time taken:', timeit.default_timer() - start_time)

def make_tuple(p1, p2):
    return tuple(map(tuple, [p1, p2]))

def play_recusive_game(p1, p2):
    previous_rounds = set() # like 50x faster
    while True:
        # end of game conditions
        if make_tuple(p1, p2) in previous_rounds:
            # print('loop achieved', p1, p2)
            winner = 1
            cards = p1
            break
        if len(p2) == 0:
            winner = 1
            cards = p1
            break
        if len(p1) == 0:
            winner = 2
            cards = p2
            break
            
        previous_rounds.add(make_tuple(p1, p2))
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        # end of round conditions
        if len(p1) >= c1 and len(p2) >= c2:
            subwinner, _ = play_recusive_game(p1[:c1], p2[:c2]) # returns 1 or 2
            if subwinner == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1) 
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
    return (winner, cards)

def part2():
    infile = 'day22eg.txt'
    infile = 'day22.txt'
    # infile = 'day22eg2.txt'
    p1, p2 = parse_decks(infile)
    winner, cards = play_recusive_game(p1, p2)
    print(winner, cards)
    score = get_score(cards)
    return score

start_time = timeit.default_timer()
print(part2())
print('Time taken:', timeit.default_timer() - start_time)
