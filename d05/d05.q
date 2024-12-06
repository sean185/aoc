inp:read0`:d05eg.txt
inp:read0`:d05.txt
// part 1
m:{y group [x]} . flip "J"$"|"vs'"\n"vs first "\n\n"vs"\n"sv inp
us:"J"$","vs'"\n"vs last "\n\n"vs"\n"sv inp
sum {x floor %[;2]count x} each us where {n:-1+count x; all {all y in m x}'[n#x;(1+til n)_\:x]} each us
// part 2
f:{n:count x; {all y in m x}'[n#x;(1+til n)_\:x]}
f2:{if[all a:f x;:x]; i:last where not a; x[i+0 1]:x[i+1 0]; x}/
sum {x floor %[;2]count x} each f2 each us where not all each f each us
