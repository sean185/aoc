import regex as re

def parse_day19(infile):
    with open(infile) as f:
        rules, txt = [chunk.splitlines() for chunk in f.read().split('\n\n')]
    rules = {k:v for k, v in [r.split(': ') for r in rules]}
    return rules, txt

def collapse(t, r):
    is_recursive = False
    # print(r, t[r])
    # t :: the set of rules
    # r :: rule id
    rule = t[r]
    # extract the base case
    if rule.startswith('"'):
        return rule.strip('"')
    result = []
    # there will only ever be 1 or 2 rules
    for part in rule.split(' | '):
        result_part = ''
        for p in part.split():
            if p == r: # part 2 scenario
                is_recursive = 'g'+p
                result_part += f'(?P>{is_recursive})'
            else:
                result_part += collapse(t, p)
        result.append(result_part)
    if is_recursive:
        return f'(?P<{is_recursive}>'+'|'.join(result)+')'
    else:
        return '(?:'+'|'.join(result)+')'

if __name__ == '__main__':
    infile = 'day19eg1.txt'
    infile = 'day19eg2.txt'
    infile = 'day19.txt'
    rules, txt = parse_day19(infile)
    
    # part 1
    regexp = '^'+collapse(rules,'0')+'$'
    result = [None != re.match(regexp, x) for x in txt]
    print(sum(result))

    # part 2
    infile = 'day19eg3.txt'
    infile = 'day19.txt'
    rules, txt = parse_day19(infile)
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
    
    regexp = '^'+collapse(rules,'0')+'$'
    print(regexp)
    result = [None != re.match(regexp, x) for x in txt]
    print(sum(result))
