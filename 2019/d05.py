class TEST():
	def __init__(self, intcodes):
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
		print(self.intcodes)
		print(self.pos, self.opcode, self.intcodes[self.pos:self.pos+6])
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
		n = input('Enter here:')
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
		print(n,v,d)
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

if __name__ == '__main__':
	with open('day5_input.txt', 'r') as f:
		intcodes = f.read()

	intcodes = list(map(int, intcodes.split(',')))
	TestCase = TEST(intcodes)
	TestCase.run()
	print(TestCase.output)