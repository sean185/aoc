\cd C:\Repos\aoc2021\d14
template:first txt:read0 `:d14eg.txt
template:first txt:read0 `:d14.txt
strs:{(x[0 1];x[0],last[x],x[1])} each 2_ txt

// part 1 - 2590
map:strs[;0]!til count strs
realmap:map[strs[;0]]!{(map x 0 1; map x 1 2)} each strs[;1]
start:map -1_ template,'next template
res:map ? 10 {raze realmap x}/start
res:asc count each group (first first res),last each res
max[res]-min res

// part 2 - 2875665202438
pairs:update mapping:(pair!i) {(x 0 1;x 1 2)} each strs[;1] from ([]pair:strs[;0])
pairs:update qty:0^(count each group (-1_ template,'next template)) pair from pairs
res:exec sum qty by last each pair from 40 {update qty:0^((+/)qty*mapping!\:1 1)[i] from x}/pairs
res[first template]+:1
max[res]-min res

