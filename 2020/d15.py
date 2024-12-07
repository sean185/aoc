import timeit

def day15(n, t):
    latest = t[-1] # initial last number
    lastpos = dict(zip(t[:-1], range(len(t)-1))) # keep track of latest positions only
    for i in range(len(t)-1, n-1):
        lastpos[latest], latest = i, i - lastpos.get(latest, i) # safe get & swap values 
    return latest

def eg():
    return day15(2020, [0, 3, 6])

def part1():
    return day15(2020, [2, 1, 10, 11, 0, 6])

def part2():
    return day15(30000000, [2, 1, 10, 11, 0, 6])

print('Running Example')
start_time = timeit.default_timer()
print(eg())
print('Time taken:', timeit.default_timer() - start_time)

print('Part 1')
start_time = timeit.default_timer()
print(part1())
print('Time taken:', timeit.default_timer() - start_time)

print('Part 2')
start_time = timeit.default_timer()
print(part2())
print('Time taken:', timeit.default_timer() - start_time)

# print('Best trial of 7 runs of 100', min(timeit.Timer(test_code+part2_run_code).repeat(7,100)))
