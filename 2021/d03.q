\cd C:\Repos\aoc2021\d03
f:`:d03eg.txt
f:`:d03.txt
// part 1 - 3687446
prd 2 sv/: {(0>x;0<x)} sum -1+2*"1"=read0 f // 2nd try

// part 2 refactored - 4406844
t:read0 f;
search:{[b;list;pos]
    if[1=count list;:list];
    g:sum -1+2*"1"=list[;pos];
    i:"01"$[0=g;b;b=0<g];
    list where i=list[;pos]
    };
n:til count first t;
res:(search[1b]/[t;n];search[0b]/[t;n]);
prd 2 sv/: first each "1"=res

\ts:1000 res:(search[1b]/[t;n];search[0b]/[t;n]);
// 20 2064

2 sv raze "1"=t
{0N!y; x inter'where each y=/:(-1 0 1!(0 1;1 0;1 0)) signum 0N!sum -1+2*y}\[2#enlist til count t[0];"1"=flip t]

\
g = majority is neg, pos, or 0
if majority is neg, use 0 --> 1 0 = 0
if majority is pos, use 1 --> 1 1 = 1
if no majority, use 1

invert the above if the alt case
if minority is neg, use 0 --> 0 0 = 1
if minority is pos, use 1 --> 0 1 = 0
if no minority, use 0
