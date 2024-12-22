init:get each read0`:d22eg.txt
init:get each read0`:d22.txt
xor:{0b sv (<>). 0b vs'(x;y)} // faster!
m:mod[;16777216]
f:{m{xor[x;x*2048]}m{xor[x;x div 32]}m{xor[x;x*64]}x}/[2000;]
sum f each init
/ part 2
f:{m{xor[x;x*2048]}m{xor[x;x div 32]}m{xor[x;x*64]}x}\[2000;]
init:1 2 3 2024 // different test case!
map:(f each init) mod 10
dmap:{p:-4_ flip 3 next\1_deltas x; x 4+first each group p} each map
max sum 0^{dmap @\:x}(distinct raze key each dmap)
