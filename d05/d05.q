inp:read0`:d05eg.txt
inp:read0`:d05.txt
// prep data
m:{y group [x]} . flip "J"$"|"vs'"\n"vs first "\n\n"vs"\n"sv inp
us:"J"$","vs'"\n"vs last "\n\n"vs"\n"sv inp
// part 1
f:{all each ((1+til count x)_\:x)in'm x}
mid:{x(count x)div 2}
sum mid each us where all each f each us
// part 2
f2:{if[all a:f x;:x]; i:last where not a; @[x;i+0 1;:;x i+1 0]}/
sum mid each f2 each us where not all each f each us
