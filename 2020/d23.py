import timeit
from memory_profiler import profile

input = '389125467'
input = '589174263'

class Cups:
    def __init__(self, input, n=None):
        # create a list whose indices point to the next cup
        input = [int(x) for x in input]
        if n and n > len(input):
            input += list(range(len(input) + 1, n + 1))
        self.parse_cups(input)
    
    def parse_cups(self, input):
        self.curr = input[0]
        cups = [0]*(len(input)+1)
        cups[input[-1]] = input[0]
        for i in range(len(input)-1):
            cups[input[i]] = input[i+1]
        self.cups = cups

    def sim(self):
        ignore_list = set([0, self.curr])
        grabbed_1 = self.cups[self.curr]
        ignore_list.add(grabbed_1) 
        grabbed_2 = self.cups[grabbed_1]
        ignore_list.add(grabbed_2)
        grabbed_3 = self.cups[grabbed_2]
        ignore_list.add(grabbed_3)
        next_cup = self.cups[grabbed_3]
        # find destination cup
        dest = self.curr - 1
        while True:
            # print(dest)
            if dest not in ignore_list and dest > 0:
                break
            dest -= 1
            if dest <= 0:
                dest = len(self.cups)-1
        dest_cup = dest
        # put back the cups in the position after the destination cup
        self.cups[grabbed_3] = self.cups[dest_cup]
        self.cups[dest_cup] = grabbed_1
        self.cups[self.curr] = next_cup
        # print(self.curr, ignore_list, dest_cup)
        self.curr = next_cup

part1 = Cups(input)
n = 100

start_time = timeit.default_timer()
for i in range(n):
    part1.sim()
print('Time taken:', timeit.default_timer() - start_time)

curr = 1
output = []
for _ in range(8):
    curr = part1.cups[curr]
    output.append(curr)
print(''.join(str(x) for x in output))

# exit()


part2 = Cups(input, 1000000)
n = 10000000

start_time = timeit.default_timer()
for i in range(n):
    part2.sim()
print('Time taken:', timeit.default_timer() - start_time)

curr = 1
product = 1
for _ in range(2):
    curr = part2.cups[curr]
    product *= curr
print(product)
