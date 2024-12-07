inp:read0`:d06eg.txt
inp:read0`:d06.txt
// part 1
d:(-1 0;0 1;1 0;0 -1) // up right down left
where2d:{(til count x),/:'where each x}
// use position vector (row;col;facing)
start:,[;0]first raze where2d inp="^"
f:{v:last x; np:(d v 2)+v 0 1; if[null t:inp . np;:x]; x,$["#"=t;enlist[(v 0 1),(1+v 2)mod 4];enlist[np,v 2]]}
count search:distinct {x[;0 1]} f/[enlist start]

// part 2
// search only along the original path
start:,[;0]first raze where2d inp="^"
f:{[g;x] v:last x; np:(d v 2)+v 0 1; if[null t:g . np;:x]; nv:$["#"=t;(v 0 1),(1+v 2)mod 4;np,v 2]; if[nv in x;'"aha"]; x,enlist nv}
sum @[{0N!x;f[.[inp;x;:;"#"];]/[enlist start];0b};;1b]each search
// runs in 5 mins T_T