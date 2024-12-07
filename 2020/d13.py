import time
stopwatch = time.time()
# with open('day13eg.txt') as f:
with open('day13.txt') as f:
    data = f.read().splitlines()

# part 1
start_time = int(data[0])
buses = [int(x) for x in data[1].split(',') if x.isnumeric()]
wait_times = [b-start_time % b for b in buses if b]
min_wait = min(wait_times)
print(min_wait*buses[wait_times.index(min_wait)])

# part 2
def find_lcm_offset(a, b, d):
    n = 1
    m = 1
    while True:
        if d+n*a == m*b:
            return m*b
        if d+n*a > m*b:
            f = ((d+n*a)-m*b)//b
            m += f if f > 0 else 1
        else:
            n += 1

buses = [(p, int(b)) for p, b in enumerate(data[1].split(',')) if b.isnumeric()]
mult = 1
result = 0
for i in range(len(buses)-1):
    curr_bus, next_bus = buses[i:i+2]
    offset = next_bus[0] - curr_bus[0] # relative offset
    mult *= curr_bus[1] # accumulate this
    result = find_lcm_offset(mult, next_bus[1], offset+result)
    # print(offset, mult, result)

print(result-next_bus[0])
print(time.time()-stopwatch)