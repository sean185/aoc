def testrun(input, noun, verb):
    intcodes = input[:] # to prevent mutating the source
    pos = 0
    intcodes[1] = noun
    intcodes[2] = verb
    isrunning = True
    while isrunning:
        opcode, n, v, d = intcodes[pos:pos+4]
        if opcode == 1:
            intcodes[d] = intcodes[n]+intcodes[v]
        if opcode == 2:
            intcodes[d] = intcodes[n]*intcodes[v]
        if opcode == 99:
            isrunning = False
        pos+=4
    return intcodes

if __name__ == '__main__':
    with open('day2_input.txt') as f:
        input = f.read()
    intcodes = list(map(int, input.split(',')))
    part1 = testrun(intcodes, 12, 2)[0]
    print(part1)
    
    base_case = testrun(intcodes,0,0)[0]
    noun_inc = testrun(intcodes,1,0)[0]-base_case
    verb_inc = testrun(intcodes,0,1)[0]-base_case
    noun, remainder = divmod(19690720-base_case, noun_inc)
    verb, remainder = divmod(remainder, verb_inc)
    part2 = noun*100+verb
    print(part2)
