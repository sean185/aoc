edges:`$"-"vs'read0`:d23eg.txt
edges:`$"-"vs'read0`:d23.txt
nodes:asc distinct raze edges
links:nodes!asc each {distinct except[;x] raze edges where any each edges=x}each nodes
/ part 1, unabashedly bruteforcing
\ts count {x where {any x like "t*"}each x} asc {distinct asc each x[;0 1 2] where (x[;0]=x[;3])&(4=sum each differ each x)} {raze x,/:'links last each x} {raze x,/:'links last each x} {raze x,/:'links last each x} nodes

/ part 2
/ max number of links is 13, so largest sub-graph is at most 14 nodes large.
/ since there must be ONLY ONE largest graph, look for nodes which have the highest degree of completeness
/ check how many nodes 1 degree away are still found 2 degrees away
r:{count v where c=max c:sum each v in/:links each asc v:links x} each nodes
","sv string asc nodes where (max r)=r
