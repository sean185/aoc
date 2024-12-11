inp:"J"$" "vs"125 17"
inp:"J"$" "vs"77 515 6779622 6 91370 959685 0 9861" // my input
f:{(),$[0=x;1;0=(count a:string x) mod 2;("J"$2 0N#a);x*2024]}
g:{select sum c by v from ungroup update f each v from x} 
sum 25 g/([] v:inp; c:1) // part 1
sum 75 g/([] v:inp; c:1) // part 2