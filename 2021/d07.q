\cd C:\Repos\aoc2021\d07
crabs:asc value first read0 `:d07eg.txt
crabs:value first read0 `:d07.txt
// part 1 - 348996
f1:{abs x-y}
min sum crabs f1\:til max crabs
\ts:100 min sum crabs f1\:til max crabs // 1396 16421488
// part 2 - 98231647
f2:{sum til 1+d:abs x-y}
min sum crabs f2/:\:til max crabs
\ts:10 min sum crabs f2/:\:til max crabs // 57017 16444144
// part 2 v2
min sum (sums til 1+max crabs)@crabs f1\:til max crabs
\ts:100 min sum (sums til 1+max crabs)@crabs f1\:til max crabs // 1723 32793552
// part 1 v2
k:key g:count each group crabs
\ts:100 min sum value g*k f1\:til max k // 1243 21308144
// part 2 v3
\ts:100 min sum value g*(sums til 1+max k)@k f1\:til max k // 1368 21324944

