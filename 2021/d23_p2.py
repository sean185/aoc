#############
#...........#
###D#A#C#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#B#B#
  #########

from pprint import pprint

# part 1
# goal = tuple(int(x) for x in '0000000000011223344')
# start = tuple(int(x) for x in '0000000000044113232')
# start = tuple(int(x) for x in '0000000000021342341')
# rooms = {
    # 1: (11, 12),
    # 2: (13, 14),
    # 3: (15, 16),
    # 4: (17, 18)
# }
# part 2
goal = tuple(int(x) for x in '000000000001111222233334444')
start = tuple(int(x) for x in '000000000004444132132123132')
# start = tuple(int(x) for x in '000000000002441332422134131')
rooms = {
    1: (11, 12, 13, 14),
    2: (15, 16, 17, 18),
    3: (19, 20, 21, 22),
    4: (23, 24, 25, 26)
}
picture = {0:'.',1:'A',2:'B',3:'C',4:'D'}
weight = {1:1,2:10,3:100,4:1000}

memo = dict()
mincost = float('Inf')

def printer(state):
    hallway = [picture[x] for x in state[:11]]
    rms = [[picture[state[x]] for x in v] for k, v in rooms.items()]
    s = [
        '#############',
        '#'+''.join(hallway)+'#',
        '###'+'#'.join([x[0] for x in rms])+'###',
        '  #'+'#'.join([x[1] for x in rms])+'#', # comment these out for part 1
        '  #'+'#'.join([x[2] for x in rms])+'#', # comment these out for part 1
        '  #'+'#'.join([x[3] for x in rms])+'#',
        '  #########  ',
        ]
    print('\n'.join(s))

def make_move(state, start, end):
    # return a new state
    tmp = list(state)
    tmp[start], tmp[end] = tmp[end], tmp[start]
    return tuple(tmp)

# def has_room_in_room(state, i, s):
    # spaces = rooms[s]
    # return all([state[x] in (0, s) for x in spaces])

def has_path_to_room(state, i, s):
    r = sorted([i, s*2])
    clear_path = all([state[x] == 0 for x in range(r[0], r[1]+1) if not x == i])
    spaces = rooms[s]
    clear_room = all([state[x] in (0, s) for x in spaces])
    return clear_path and clear_room

def move_to_room(state, i, s):
    # i is a position in a hallway
    spaces = rooms[s]
    num = abs(i - s*2)
    j = spaces[-1]
    while j > 0:
        if state[j] == 0:
            newstate = make_move(state, i, j)
            num += spaces.index(j) + 1
            break
        j -= 1
    return newstate, num * weight[s]

def is_blocked(state, i, s):
    pass

def get_valid_hallways(state, i, s):
    # i is a position in a room
    r = 1+int((i-11)/len(rooms[1]))
    door = r*2
    positions = []
    spaces = rooms[r]    # print(i, s, r)
    # is a partially complete room, assuming filled correctly
    if all([state[x] in (0, r) for x in spaces]):
        return []
    # is blocked if not the first, and the preceeding is blocked
    if (not i == spaces[0]) and (state[i-1] != 0):
        return []
    for j, t in enumerate(state[:11]):
        if (j in {2, 4, 6, 8}) or (t != 0):
            continue
        r = sorted([door, j])
        clear_path = all([state[x] == 0 for x in range(r[0], r[1]+1)])
        if not clear_path:
            continue
        newstate = make_move(state, i, j)
        num = abs(door - j) 
        num += 1 + i - spaces[0] # front or back of room
        positions.append((newstate, num * weight[s]))
    return positions

def part1(state, cost=0):
    # print('----------newstep----------')
    # printer(state)
    # returns a list of costs if any
    global mincost
    # minimization 
    if cost > mincost:
        return []
    # objective
    if state == goal:
        if cost < mincost:
            mincost = cost
            print('SOLVED!', mincost)
        return [cost]
    # memoization
    k = state+(cost,)
    if k in memo:
        return memo[k]
    # trying every possibility
    possibilities = []
    for i, s in enumerate(state):
        if s == 0:
            continue
        if i < 11:
            # handle hallway amphipods
            if has_path_to_room(state, i, s):
                newstate, newcost = move_to_room(state, i, s)
                possibilities.append((newstate, cost+newcost))
        else:
            # handle room amphipods
            for newstate, newcost in get_valid_hallways(state, i, s):
                possibilities.append((newstate, cost+newcost))
    results = []
    # print(len(possibilities))
    for p in possibilities:
        results.extend(part1(*p))
    memo[k] = results
    return results

print(min(part1(start)))
