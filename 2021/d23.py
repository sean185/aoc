#############
#...........#
###D#A#C#C###
  #D#A#B#B#
  #########

from pprint import pprint 

hallway = ['.']*11
doorway = (2,4,6,8)
start_rooms = [['D','D'],['A','A'],['C','B'],['C','B']] # a room is really a FILO queue of depth 2
start_rooms = [['B','A'],['C','D'],['B','C'],['D','A']] # a room is really a FILO queue of depth 2
goal = [['A','A'],['B','B'],['C','C'],['D','D']]
weight = {'A':1, 'B':10, 'C':100, 'D':1000}

check_empty = lambda x: all([i == '.' for i in x])
check_has = lambda x, y: x == ['.', '.'] or x == ['.', y]
rbetween = lambda x, y: range(x, y+1) if x < y else range(y, x+1)
mincost = float('Inf')

def add2room(room, s):
    if room[1] == '.':
        room[1] = s
        return 2
    else:
        room[0] = s
        return 1

def dupestate(hallway, rooms):
    return (hallway[:], [r[:] for r in rooms[:]])

def printer(hallway, rooms):
    s = [
        '#############',
        '#'+''.join(hallway)+'#',
        '###'+'#'.join([x[0] for x in rooms])+'###',
        '  #'+'#'.join([x[1] for x in rooms])+'#',
        '  #########  ',
        ]
    print('\n'.join(s))

memo = dict()
    
def part1(hallway, rooms, steps=0):
    global mincost
    # print('-----newstep----')
    # print(steps)
    # printer(hallway, rooms)
    # print('----------------')
    # returns a series of steps that succeed: [('A',10),('B',4)]
    # compute valid moves/steps, and recurse
    k = tuple(hallway + rooms[0] + rooms[1] + rooms[2] + rooms[3] + [steps])
    if steps >= mincost:
        return []
    if k in memo:
        # print('cache hit!')
        return memo[k]
    if rooms == goal:
        print('done!', steps)
        if steps < mincost:
            mincost = steps
        # print(steps)
        # printer(hallway, rooms)l
        return [steps]
    possibilities = []
    # if it is in a hallway, try and put into a room
    for i, s in enumerate(hallway):
        if s == '.':
            continue
        d = ('A','B','C','D').index(s)
        if check_empty([hallway[h] for h in rbetween(doorway[d], i) if h != i]) and check_has(rooms[d], s):
            # print('hallway to available rooms?')
            num = abs(doorway[d] - i)
            newhallway, newrooms = dupestate(hallway, rooms)
            newhallway[i] = '.'
            num += add2room(newrooms[d], s)
            possibilities.append([newhallway, newrooms, steps + weight[s]*num])
    # if it is in a room, try and put into its room or a hallway
    for i, r in enumerate(rooms):
        rpos = doorway[i]
        if r == goal[i]:
            # nothing to do, what to return?
            continue
        if r[0] != '.':
            s = r[0]
            d = ('A','B','C','D').index(s)
            # check its room, if possible, then done
            if check_empty([hallway[h] for h in rbetween(rpos, doorway[d])]) and check_has(rooms[d], s):
                # print('checking for available room 0!', s)
                newhallway, newrooms = dupestate(hallway, rooms)
                newrooms[i][0] = '.'
                num = abs(rpos - doorway[d]) + 1
                num += add2room(newrooms[d], s)
                possibilities.append([newhallway, newrooms, steps + weight[s]*num])
                continue
            # check hallway
            for j, c in enumerate(hallway):
                if j in doorway or c != '.':
                    continue
                # print('checking for available hall space 0!', s)
                check_empty([hallway[h] for h in rbetween(rpos, j)])
                newhallway, newrooms = dupestate(hallway, rooms)
                newrooms[i][0] = '.'
                newhallway[j] = s
                num = abs(rpos - j) + 1
                possibilities.append([newhallway, newrooms, steps + weight[s]*num])
        elif r[1] != '.':
            s = r[1]
            d = ('A','B','C','D').index(s)
            if i == d:
                continue
            # check its room
            if check_empty([hallway[h] for h in rbetween(rpos, doorway[d])]) and check_has(rooms[d], s):
                # print('checking for available room 1!', s, i, rpos, d)
                newhallway, newrooms = dupestate(hallway, rooms)
                newrooms[i][1] = '.'
                num = abs(rpos - doorway[d]) + 2
                num += add2room(newrooms[d], s)
                possibilities.append([newhallway, newrooms, steps + weight[s]*num])
                continue
            # check hallway
            for j, c in enumerate(hallway):
                if j in doorway or c != '.' and not check_empty([hallway[h] for h in rbetween(rpos, j)]):
                    continue
                # print('checking for available hall space 1!', s)
                newhallway, newrooms = dupestate(hallway, rooms)
                newrooms[i][1] = '.'
                newhallway[j] = s
                num = abs(rpos - j) + 2
                possibilities.append([newhallway, newrooms, steps + weight[s]*num])
    # pprint(possibilities)
    results = []
    for p in possibilities:
        results.extend(part1(*p))
    memo[k] = results
    return results

final = part1(hallway, start_rooms)
print(min(final))