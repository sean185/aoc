inp:", "vs first read0`:d01.txt
// part 1
d:(1 0;0 1;-1 0;0 -1) // north east south west
sum 2# 0 0 0{x[2]:mod[;4]x[2]+("RL"!1 -1)y[0]; x[0 1]+:("J"$1_y)*d x[2]; x}/inp
// part 2
G:enlist 0 0;
0 0 0{x[2]:mod[;4]x[2]+("RL"!1 -1)y[0]; n:"J"$1_y; {if[x in G;'-3!x]; G,:enlist x}each 0N!x[0 1]+/:(d x 2)*/:1+til n; x[0 1]+:n*d x[2]; x}/inp
