\cd C:\Repos\aoc2021\d19
scans:{value each 1_ "\n" vs x} each "\n\n" vs "\n" sv read0 `:d19.txt;
scans:{value each 1_ "\n" vs x} each "\n\n" vs "\n" sv read0 `:d19eg.txt;
mm:{sum flip x*\:y};
// rx, ry, rz
rotax:{
    if[0>type x; x:1#x];
    if[null first x; :y];
    rotations:((1 0 0;0 0 -1;0 1 0);(0 0 1;0 1 0;-1 0 0);(0 -1 0;1 0 0;0 0 1)) x;
    {mm[y;x]}/[y;rotations]
    };
/ rotax[0 0 0 0;1 2 3]
/ s, 0, 0, 0
/ s+1, 0, 0, 0
/ s+1+1, 0, 0, 0
/ s+1+1+1, 0, 0, 0
/ s+1+2, 0, 0, 0
/ s+1+2+2+2, 0, 0, 0
rots:(
    0N;0;0 0;0 0 0;
    1;1 0;1 0 0;1 0 0 0;
    1 1;1 1 0;1 1 0 0;1 1 0 0 0;
    1 1 1;1 1 1 0;1 1 1 0 0;1 1 1 0 0 0;
    1 2;1 2 0;1 2 0 0;1 2 0 0 0;
    1 2 2 2;1 2 2 2 0;1 2 2 2 0 0;1 2 2 2 0 0 0);

rotateall:{flip ({rotax[x;]} each rots)@\:/:x};

match:{[x;y]
    / returns a table that can be empty
    maxcombs:raze {1#desc count each group raze x} each scans[x]-\:/:/:r:rotateall scans[y];
    res:update rotidx:i from ([]src:x; dest:y; displacement:key maxcombs; matches:value maxcombs;points:r);
    select from res where matches >= 12
 };

jumps:{
    search:1_ til count scans;
    res:upd:raze match[0;] each search;
    while[count search;
        seed:desc exec distinct dest from upd;
        search:search except exec distinct (src, dest) from res;
        res,:upd:raze match ./: seed cross search
    ];
    res
 }[];

// align all frames of reference to scanner 0, then apply
// accumulate list of jumps and rotations required to traverse back

pretransform:([]points:scans),'{
    if[0=x[`frame];:x]; 
    t:first select from jumps where dest=x[`frame]; 
    `frame`hops`turns!(t[`src];x[`hops],enlist t[`displacement];x[`turns],t[`rotidx])
    }/'[{`frame`hops`turns!(x;();())} each til count scans]

// part 1 - 378
count asc distinct raze exec points from 
update points:absdisp+/:'{{rotax[rots y;] each x}/[x;y]}'[scans;turns] from
res:update absdisp:{{y+rotax[rots z;x]}/[0 0 0;x;y]}'[hops;turns] from pretransform

// part 2 - 
max {c:til count x; {sum abs y-x} ./: x c cross c} exec absdisp from res
