import itertools 
class TEST():
    def __init__(self, inputs, intcodes):
        self.inputs = inputs
        self.intcodes = intcodes
        self.pos = 0 
        self.isrunning = True
        self.output = []

    def run(self):
        while self.isrunning:
            self.step()

    def step(self):
        self.opcode = str(self.intcodes[self.pos]).zfill(5)
        self.optype = self.opcode[-2:]
        ignore, self.v_mode, self.n_mode = self.opcode[:3]
        # print(self.intcodes)
        # print(self.pos, self.opcode, self.intcodes[self.pos:self.pos+6])
        if self.optype == '99':
            self.isrunning = False
        else:
            getattr(self, 'doop'+self.optype)()

    def retrieve(self, mode, val):
        if mode == '0':
            return self.intcodes[val]
        elif mode == '1':
            return val
        else:
            pass # catch err?

    def doop01(self):
        n,v,d = self.intcodes[self.pos+1:self.pos+4]
        n = self.retrieve(self.n_mode, n)
        v = self.retrieve(self.v_mode, v)
        self.intcodes[d] = n + v
        self.pos+=4

    def doop02(self):
        n,v,d = self.intcodes[self.pos+1:self.pos+4]
        n = self.retrieve(self.n_mode, n)
        v = self.retrieve(self.v_mode, v)
        self.intcodes[d] = n * v
        self.pos+=4
        
    def doop03(self):
        n = self.inputs.pop(0)
        p = self.retrieve('0',self.pos+1)
        self.intcodes[p] = int(n)
        self.pos+=2

    def doop04(self):
        n = self.intcodes[self.pos+1]
        self.output.append(self.intcodes[n])
        self.pos+=2

    def doop05(self):
        # jump if true
        n, v = self.intcodes[self.pos+1:self.pos+3]
        n = self.retrieve(self.n_mode, n)
        v = self.retrieve(self.v_mode, v)
        if n == 0:
            self.pos+=3
        else:
            self.pos = v

    def doop06(self):
        # jump if false
        n, v = self.intcodes[self.pos+1:self.pos+3]
        n = self.retrieve(self.n_mode, n)
        v = self.retrieve(self.v_mode, v)
        if n == 0:
            self.pos = v
        else:
            self.pos+=3

    def doop07(self):
        n,v,d = self.intcodes[self.pos+1:self.pos+4]
        n = self.retrieve(self.n_mode, n)
        v = self.retrieve(self.v_mode, v)
        self.intcodes[d] = int(n<v)
        self.pos+=4

    def doop08(self):
        n,v,d = self.intcodes[self.pos+1:self.pos+4]
        n = self.retrieve(self.n_mode, n)
        v = self.retrieve(self.v_mode, v)
        self.intcodes[d] = int(n==v)
        self.pos+=4

def runamps(intcodes, inputs1):
    input2 = 0
    for i in range(len(inputs1)):
        # print(input2, inputs1)
        TestCase = TEST([inputs1.pop(0), input2], intcodes[:])
        TestCase.run()
        input2 = TestCase.output[0]
    return input2

if __name__ == '__main__':
    # INPUTS = [4,3,2,1,0] # sample1
    # with open('day7_sample1.txt', 'r') as f:
        # intcodes = f.read()

    # INPUTS = [0,1,2,3,4] # sample2
    # with open('day7_sample2.txt', 'r') as f:
        # intcodes = f.read()

    # INPUTS = [1,0,4,3,2] # sample3
    # with open('day7_sample3.txt', 'r') as f:
        # intcodes = f.read()

    with open('day7_input.txt', 'r') as f:
        intcodes = f.read()
    intcodes = list(map(int, intcodes.split(',')))

    lastmax = 0
    for config in itertools.permutations(range(5)):
        result = runamps(intcodes[:], list(config))
        if result > lastmax:
            lastmax = result
            lastmaxconfig = config
    print(lastmax, lastmaxconfig)
