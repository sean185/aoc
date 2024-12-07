inp:read0`:d02.txt
// part 1
f:{(all 1_ deltas[x] within 1 3) or (all 1_ deltas[reverse x] within 1 3)}
sum f each {"J"$" "vs x}each inp
// part 2
sum {$[f x;1b;any f each x _/:til count x]} each {"J"$" "vs x}each inp
