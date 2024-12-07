filename = 'd03.txt'
with open(filename) as f:
    txt = f.read().splitlines()
txt = "".join(txt)

# part 1
# example
# txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
def extract(s):
    tot = 0
    op, l, r = (0, "", "")
    for c in s:
        if op == 0 and c == "m":
            op = 1
        elif op == 1 and c == "u":
            op = 2
        elif op == 2 and c == "l":
            op = 3
        elif op == 3 and c == "(":
            op = 4
        elif op == 4:
            if c.isnumeric():
                l += c
            elif c == "," and l.isnumeric():
                l = int(l)
                op = 5
            else:
                op, l, r = (0, "", "") # reset 
        elif op == 5:
            if c.isnumeric():
                r += c
            elif c == ")" and r.isnumeric():
                r = int(r)
                tot += l*r
                op, l, r = (0, "", "") # reset 
            else:
                op, l, r = (0, "", "") # reset 
        else:
            op = 0
    return tot

print(extract(txt))

# part 2
# example
# txt = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
def extract(s):
    tot = 0
    flag = True
    op, l, r = (0, "", "")
    for c in s:
        if op == 0 and c == "m":
            op = 1
        elif op == 1 and c == "u":
            op = 2
        elif op == 2 and c == "l":
            op = 3
        elif op == 3 and c == "(":
            op = 4
        elif op == 4:
            if c.isnumeric():
                l += c
            elif c == "," and l.isnumeric():
                l = int(l)
                op = 5
            else:
                op, l, r = (0, "", "") # reset 
        elif op == 5:
            if c.isnumeric():
                r += c
            elif c == ")" and r.isnumeric():
                r = int(r)
                tot += l*r if flag else 0
                op, l, r = (0, "", "") # reset 
            else:
                op, l, r = (0, "", "") # reset 
        elif op == 0 and c == "d":
            op = 6
        elif op == 6 and c == "o":
            op = 7
        elif op == 7 and c == "(":
            op = 8
        elif op == 8 and c == ")":
            flag = True
            op = 0
        elif op == 7 and c == "n":
            op = 9
        elif op == 9 and c == "'":
            op = 10
        elif op == 10 and c == "t":
            op = 11
        elif op == 11 and c == "(":
            op = 12
        elif op == 12 and c == ")":
            flag = False
            op = 0
        else:
            op = 0
    return tot

print(extract(txt))
