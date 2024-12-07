def hex2binstr(x):
    return bin(int(x, 16))[2:].zfill(len(x)*4)

def parser(x):
    V = int(x[0:3], 2)
    T = int(x[3:6], 2)
    x = x[6:]
    pl = 6
    if T == 4:
        literals = ''
        carryon = True
        while carryon:
            carryon = x[0] == '1'
            literals += x[1:5]
            x = x[5:]
            pl += 5
        return (V, T, pl, int(literals,2))
    else:
        arr = []
        n = 16 if x[0] == '0' else 12
        L = int(x[1:n], 2)
        x = x[n:]
        pl += n
        if n == 16:
            while L > 6:
                sub = parser(x)
                x = x[sub[2]:]
                pl += sub[2]
                L -= sub[2]
                arr.append(sub)
        else:
            for _ in range(L):
                sub = parser(x)
                x = x[sub[2]:]
                pl += sub[2]
                arr.append(sub)
        return (V, T, pl, arr)

def part1(x):
    if type(x[3]) == list:
        return x[0] + sum([part1(y) for y in x[-1]])
    else:
        return x[0]

def part2(x):
    if x[1] == 4:
        return x[3]
    else:
        values = [part2(y) for y in x[3]]
    if x[1] == 0:
        return sum(values)
    elif x[1] == 1:
        prd = 1
        for p in values:
            prd *= p
        return prd
    elif x[1] == 2:
        return min(values)
    elif x[1] == 3:
        return max(values)
    elif x[1] == 5:
        return int(values[0] > values[1])
    elif x[1] == 6:
        return int(values[0] < values[1])
    elif x[1] == 7:
        return int(values[0] == values[1])

d16 = 'C20D7900A012FB9DA43BA00B080310CE3643A0004362BC1B856E0144D234F43590698FF31D249F87B8BF1AD402389D29BA6ED6DCDEE59E6515880258E0040A7136712672454401A84CE65023D004E6A35E914BF744E4026BF006AA0008742985717440188AD0CE334D7700A4012D4D3AE002532F2349469100708010E8AD1020A10021B0623144A20042E18C5D88E6009CF42D972B004A633A6398CE9848039893F0650048D231EFE71E09CB4B4D4A00643E200816507A48D244A2659880C3F602E2080ADA700340099D0023AC400C30038C00C50025C00C6015AD004B95002C400A10038C00A30039C0086002B256294E0124FC47A0FC88ACE953802F2936C965D3005AC01792A2A4AC69C8C8CA49625B92B1D980553EE5287B3C9338D13C74402770803D06216C2A100760944D8200008545C8FB1EC80185945D9868913097CAB90010D382CA00E4739EDF7A2935FEB68802525D1794299199E100647253CE53A8017C9CF6B8573AB24008148804BB8100AA760088803F04E244480004323BC5C88F29C96318A2EA00829319856AD328C5394F599E7612789BC1DB000B90A480371993EA0090A4E35D45F24E35D45E8402E9D87FFE0D9C97ED2AF6C0D281F2CAF22F60014CC9F7B71098DFD025A3059200C8F801F094AB74D72FD870DE616A2E9802F800FACACA68B270A7F01F2B8A6FD6035004E054B1310064F28F1C00F9CFC775E87CF52ADC600AE003E32965D98A52969AF48F9E0C0179C8FE25D40149CC46C4F2FB97BF5A62ECE6008D0066A200D4538D911C401A87304E0B4E321005033A77800AB4EC1227609508A5F188691E3047830053401600043E2044E8AE0008443F84F1CE6B3F133005300101924B924899D1C0804B3B61D9AB479387651209AA7F3BC4A77DA6C519B9F2D75100017E1AB803F257895CBE3E2F3FDE014ABC'

p1_egs = ['D2FE28', '38006F45291200', 'EE00D40C823060', '8A004A801A8002F478', '620080001611562C8802118E34', 'C0015000016115A2E0802F182340', 'A0016C880162017C3686B18A3D4780']
for t in p1_egs:
    print(part1(parser(hex2binstr(t))))

print(part1(parser(hex2binstr(d16))))

p2_egs = ['C200B40A82', '04005AC33890', '880086C3E88112', 'CE00C43D881120', 'D8005AC2A8F0', 'F600BC2D8F', '9C005AC2F8F0', '9C0141080250320F1802104A08']
for t in p2_egs:
    print(part2(parser(hex2binstr(t))))

print(part2(parser(hex2binstr(d16))))
