start:0 0; end:6 6; n:12;grid:7 7#".";blocks:get each read0`:d18eg.txt
start:0 0; end:70 70; n:1024;grid:71 71#".";blocks:get each read0`:d18.txt
d:(1 0;-1 0;0 1;0 -1);
// part 1 - simulate a fixed point in time!
part1:grid .[;;:;"#"]/n#blocks
// flood fill to every node then pick end
f:{
    curr:x[0]; visited:x[1]; // update minimum of surrounding +1
    np:distinct np where (not np in\: key visited) and "."=part1 ./:np:raze curr+/:\:d;
    visited,:([node:np]val:(count np)#1+first max visited);
    if[count select from visited where (any each node<\:start)or(any each node>\:end);show visited;'"huh"?];
    (np;visited)
 }
@[;end] last f/[(enlist 0 0;([node:enlist 0 0]val:1#0))]
// part 2 - can I do a binary search?
g:{part1::grid .[;;:;"#"]/x#blocks; first @[;end] last f/[(enlist 0 0;([node:enlist 0 0]val:1#0))] }
res:{[f;l] c:count l; if[c=1;:first l]; m:c div 2; $[null f l m; .z.s[f;(m)#l] ; .z.s[f;(m)_l]]}[g;til count blocks]
blocks res // 38,63
