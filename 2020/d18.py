def parse_tokens(string):
    tokens = []
    for i in range(len(string)):
        char = string[i]
        if char in '()*+':
            tokens.append(char)
        elif char.isnumeric():
            if i > 0 and tokens[-1].isnumeric():
                tokens[-1] += char
            else:
                tokens.append(char)
    return tokens

def eval_pluses(tmp):
    tokens = tmp.copy()
    i = 0
    while i < len(tokens):
        if tokens[i] == '+':
            if not (tokens[i-1].isnumeric() and tokens[i+1].isnumeric()):
                i += 1
                continue
            op = tokens.pop(i)
            right = tokens.pop(i)
            left = tokens.pop(i-1)
            tokens.insert(i-1, str(eval(left + op + right)))
            i -= 1
        i += 1
    return tokens

def eval_lefttoright(tmp):
    tokens = tmp.copy()
    i = 0
    while i < len(tokens):
        if not (tokens[i-1].isnumeric() and tokens[i+1].isnumeric()):
            i += 1
            continue
        op = tokens.pop(i)
        right = tokens.pop(i)
        left = tokens.pop(i-1)
        tokens.insert(i-1, str(eval(left + op + right)))
    return tokens

def find_close_bracket(tokens):
    depth = 0
    if tokens[0] != '(':
        return tokens # ???
    for i in range(len(tokens)):
        if tokens[i] == '(':
            depth += 1
        if tokens[i] == ')':
            depth -= 1
        if depth == 0:
            return i

def find_top_level_brackets(tokens):
    depth = 0 
    pairs = []
    for i in range(len(tokens)):
        if tokens[i] == '(':
            if depth == 0:
                pairs.append((i,))
            depth += 1
        if tokens[i] == ')':
            depth -= 1
            if depth == 0:
                pairs[-1] += (i,)
    return pairs

def eval_part(fn, tokens):
    tlb = find_top_level_brackets(tokens)
    if len(tlb) > 0:
        result = []
        bracket_evals = [eval_part(fn, tokens[b[0]+1:b[1]]) for b in tlb]
        ignored = []
        for b in tlb:
            ignored.extend(range(b[0]+1, b[1]+1))
        replaced = [b[0] for b in tlb]
        for i, t in enumerate(tokens):
            if i in ignored:
                continue
            elif i in replaced:
                result.append(bracket_evals.pop(0))
            else:
                result.append(t)
        tokens = result
    result = fn(tokens)
    return str(eval(''.join(result)))

def eval_part1(tokens):
    tlb = find_top_level_brackets(tokens)
    if len(tlb) > 0:
        result = []
        bracket_evals = [eval_part1(tokens[b[0]+1:b[1]]) for b in tlb]
        ignored = []
        for b in tlb:
            ignored.extend(range(b[0]+1, b[1]+1))
        replaced = [b[0] for b in tlb]
        for i, t in enumerate(tokens):
            if i in ignored:
                continue
            elif i in replaced:
                result.append(bracket_evals.pop(0))
            else:
                result.append(t)
        tokens = result
    result = eval_lefttoright(tokens)
    return str(eval(''.join(result)))

def eval_part2(tokens):
    tlb = find_top_level_brackets(tokens)
    if len(tlb) > 0:
        result = []
        bracket_evals = [eval_part2(tokens[b[0]+1:b[1]]) for b in tlb]
        ignored = []
        for b in tlb:
            ignored.extend(range(b[0]+1, b[1]+1))
        replaced = [b[0] for b in tlb]
        for i, t in enumerate(tokens):
            if i in ignored:
                continue
            elif i in replaced:
                result.append(bracket_evals.pop(0))
            else:
                result.append(t)
        tokens = result
    result = eval_pluses(tokens)
    return str(eval(''.join(result)))

if __name__ == '__main__':
    with open('day18.txt') as f:
        txt = f.read().splitlines()
    total = 0
    for t in txt:
        tokens = parse_tokens(t.replace(' ',''))
        # res = eval_part1(tokens)
        res = eval_part(eval_lefttoright, tokens)
        total += int(res)
    print(total)
    total = 0
    for t in txt:
        tokens = parse_tokens(t.replace(' ',''))
        # res = eval_part2(tokens)
        res = eval_part(eval_pluses, tokens)
        total += int(res)
    print(total)
