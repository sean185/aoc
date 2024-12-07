\cd C:\Repos\aoc2021\d20
alg:"#"=first txt:read0`:d20eg.txt; 
alg:"#"=first txt:read0`:d20.txt;
pic:"#"=2_ txt;

d:-1 0 1 cross -1 0 1
reduce:{1_' -1_' 1_ -1_ x}
enhance:{yc:count x; xc:count first x; (xc;yc)#alg 2 sv/: flip x ./:/: (til[yc] cross til[xc])+\:/:d}
expand:{c:count first y:x,'y,'x;l:enlist c#x;l,y,l}

// part 1 - 5479
sum raze reduce reduce enhance expand[1b;] expand[1b;] expand[1b;] reduce reduce enhance expand[0b;] expand[0b;] expand[0b;] pic
part1:{inf:0b; do[y; x:reduce reduce enhance expand[inf;] expand[inf;] expand[inf;] x; if[alg[0]; inf:not inf]]; x}
sum raze part1[pic;2]

// part 2 - 19012
sum raze part1[pic;50]
