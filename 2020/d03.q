grid:"#"=read0`:day3.txt
slope:3 1
// part 1
findtrees:{[g;s] l:count g; w:count first g; sum g ./: {x[1],x[0] mod w} each +\[0 0;l#enlist s]}
findtrees[grid;slope]
// part 2
slopes:(1 1;3 1;5 1;7 1;1 2)
prd `long$findtrees each slopes
