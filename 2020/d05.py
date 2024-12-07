import time
start = time.time()

with open('day5.txt') as f:
    data = f.read().splitlines()

def decode_seat(code):
    row = int(code[:7].replace('F','0').replace('B','1'),2)
    col = int(code[-3:].replace('L','0').replace('R','1'),2)
    return (row, col)

# test_cases = ['FBFBBFFRLR','BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
# for t in test_cases:
    # row, col = decode_seat(t)
    # print(row*8+col)

seat_ids = []
for d in data:
    row, col = decode_seat(d)
    seat_ids.append(row*8+col)

# part 1
print(max(seat_ids))

# part 2
print(set(list(range(min(seat_ids),max(seat_ids)))).difference(set(seat_ids)))

print('time taken', time.time()-start, 'secs')