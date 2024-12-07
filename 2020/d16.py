import timeit

def parse_constraint(l):
    attr, ranges = l.split(': ')
    range1, range2 = ranges.split(' or ')
    range1 = [int(x) for x in range1.split('-')]
    range2 = [int(x) for x in range2.split('-')]
    return { 'attr':attr, 'r1':range1, 'r2':range2 }

if __name__ == '__main__':
    infile = 'day16eg.txt'
    infile = 'day16.txt'
    # infile = 'day16eg2.txt'
    with open(infile) as f:
        constraints, myticket, nearbytickets = f.read().split('\n\n')
    constraints = [parse_constraint(c) for c in constraints.splitlines()]
    myticket = [int(x) for x in myticket.splitlines()[1].split(',')]
    nearbytickets = [[int(x) for x in l.split(',')] for l in nearbytickets.splitlines()[1:]]

    # part 1
    possible_numbers = []
    for c in constraints:
        start, end = c['r1']
        possible_numbers.extend(range(start, end+1))
        start, end = c['r2']
        possible_numbers.extend(range(start, end+1))
    possible_numbers = set(possible_numbers)
    
    invalid_sum = 0
    remaining_tickets = []
    for ticket in nearbytickets:
        is_invalid = False
        for field in ticket:
            if not field in possible_numbers:
                invalid_sum += field
                is_invalid = True
        if not is_invalid:
            remaining_tickets.append(ticket)
    
    print(invalid_sum)
    
    # part 2
    tickets_by_field = list(zip(*remaining_tickets))
    from pprint import pprint 
    # for each field, check which validations it has passed
    result = {}
    for idx, field in enumerate(tickets_by_field):
        field_validation = []
        for i, c in enumerate(constraints):
            is_valid = all([(c['r1'][0] <= f <= c['r1'][1]) or (c['r2'][0] <= f <= c['r2'][1]) for f in field])
            if is_valid:
                field_validation.append(c['attr'])
                # field_validation.append(i)
        result[idx] = field_validation
    
    # pprint(result)

    final = {}
    for i in range(len(result)):
        for k, v in result.items():
            if len(v) == 1:
                m = result.pop(k)[0]
                final[k] = m
                break
        for k, v in result.items():
            v.pop(v.index(m))

    pprint(final)
    part2 = 1
    for k, v in final.items():
        if v.startswith('departure'):
            part2 *= myticket[k]
    print(part2)
