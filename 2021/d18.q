mag:{$[-7h=type x; x; sum 3 2 * .z.s each x]};
getidx:{t:type each x; raze ($[0>t 0; enlist 1#0; 0,/:.z.s x 0]; $[0>t 1; enlist 1#1; 1,/:.z.s x 1])};
explode:{
    idxs:getidx x;
    expIDX:where 4<count each idxs;
    if[0=count expIDX; :x];
    expIDX:2#expIDX;
    expLR:x ./: idxs expIDX;
    side:-1_ first idxs expIDX;
    remidx:where (-1 1 + expIDX) in til count idxs;
    .[;side;:;0] .[;;+;]/[x;idxs (-1 1 + expIDX) remidx;expLR remidx]
    };
split:{
    idxs:getidx x;
    target:idxs pos:first where 9<x ./: idxs;
    if[null pos; :x];
    buddy:(-1_target),side:1 0 last target;
    newpair:(floor;ceiling)@\: (x . target)%2;
    result:$[side;::;reverse] (newpair;x . buddy);
    $[1=count target;
        result;
        .[x;-1_target;:;result]
        ]
    };

part1:{{new:explode x; $[new~x; split new; new]}/[(x;y)]}
part1/[((1;1);(2;2);(3;3);(4;4))]
part1/[((1;1);(2;2);(3;3);(4;4);(5;5))]
part1/[((1;1);(2;2);(3;3);(4;4);(5;5);(6;6))]
part1/[(((((9;8);1);2);3);4)]
part1/[(((((4;3);4);4);(7;((8;4);9)));(1;1))]

\cd C:\Repos\aoc2021\d18
parseline:{value ssr[;"[[]";"("] ssr[;"[]]";")"] ssr[;",";";"] x}
mag part1/[eg:parseline each read0`:d18eg.txt]
mag part1/[d18:parseline each read0`:d18.txt]
max mag each part1/'[eg {x where not (=/')x} c cross c:til count eg]
max mag each part1/'[d18 {x where not (=/')x} c cross c:til count d18]
