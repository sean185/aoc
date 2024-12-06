inp:read0`:d06eg.txt
inp:read0`:d06.txt
// part 1
n:count inp
start:,[;0]{first[v],first x v:where 0<count each x} where each inp="^"
d:(-1 0;0 1;1 0;0 -1) // up right down left
f:{nxt:(d x 2)+x[0 1]; t:inp . nxt; $[null t; x; "#"=t; x[0 1],(1+x 2) mod 4; nxt,x 2]}
inp {.[x;y;:;"X"]}/{x[;0 1]}41 f\start
count search:distinct {x[;0 1]} f\[start]
// part 2
// search each position on the grid that isn't occupied
// return if looped or exited
// shamefully using a global variable for checking loop
f:{[grid;pos] if[pos in G;:pos]; nxt:(d pos 2)+pos[0 1]; t:grid . nxt; if[null t;:pos]; G,:enlist pos; $["#"=t; pos[0 1],(1+pos 2) mod 4; nxt,pos 2]}
f2:{[o] 0N!o; grid:.[inp;o;:;"#"]; G::enlist 0N 0N 0N; r:f[grid;]/[start]; r in G} 
sum f2 each search
