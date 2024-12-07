egs1:("D2FE28";"38006F45291200";"EE00D40C823060";"8A004A801A8002F478";"620080001611562C8802118E34";"C0015000016115A2E0802F182340";"A0016C880162017C3686B18A3D4780")
egs2:("C200B40A82";"04005AC33890";"880086C3E88112";"CE00C43D881120";"D8005AC2A8F0";"F600BC2D8F";"9C005AC2F8F0";"9C0141080250320F1802104A08")

\cd C:\Repos\aoc2021\d16
d16:first read0 `:d16.txt

parselit:{p:1+first where not first each l:0N 5#x;(p*5;2 sv c:raze p#1_'l)}

/ recursive parser
parser:{
    v:2 sv x 0 1 2; 
    t:2 sv x 3 4 5;
    0N!(v;t);
    x:6_ x;
    // returns values, is a terminating condition
    if[4=t; // parse and return literal value
        lit:parselit x;
        :(v;t;6+lit 0;lit 1)
    ];
    // operator with sub packets
    subs:();
    n:2 sv x 1+til (15 11)L:x 0;
    x:(1+(15 11)L)_ x;
    $[L;
        [
            // parse and by num packets
            do[n;
                res:.z.s x;
                subs,:enlist 0N!res;
                x:res[2]_ x
            ]
        ];
        [
            // parse and by packets length
            while[n > 3;
                res:.z.s x;
                subs,:enlist 0N!res;
                n:n-res[2];
                x:res[2]_ x
            ]
        ]
    ];
    (v;t;(7+(15 11)L)+sum subs[;2]; subs)
 }

part1:{$[0h=type x[3]; x[0]+sum part1 each x[3]; x[0]]}
{part1 parser raze -4#'0b vs'x} each "0123456789ABCDEF" ? egs1
part1 parser {raze -4#'0b vs'x} "0123456789ABCDEF" ? d16

part2:{
    m:(til 8)!(sum;prd;min;max;::;>/;</;=/);
    m[t] $[4=t:x 1;x 3;part2 each x 3]
 }
{part2 parser raze -4#'0b vs'x} each "0123456789ABCDEF" ? egs2
part2 parser {raze -4#'0b vs'x} "0123456789ABCDEF" ? d16
