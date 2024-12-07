\cd C:\Repos\aoc2021\d25
grid:read0`:d25eg.txt
grid:read0`:d25.txt
move:{[x;y]1_-1_ ssr[;y,".";".",y] last[x],x,first x}
moveright:{move[;">"] each x}
movedown:{flip move[;"v"] each flip x}
part1:{movedown moveright x}
{new:part1 x; i:1; while[not new ~ x; x:new; new:part1 x; i+:1]; i} grid
