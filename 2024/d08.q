inp:read0`:d08.txt
inp:read0`:d08eg.txt
// part 1
// group points by letter
// cross thier positions
// get antinodes
// filter down to bounds
where2d:{raze (til count x),/:'where each x}
antn:{(x+d;y-d:x-y)}
bounded:{sum all each x within \:\:(0;-1+count inp)}
f:{except[;b] distinct raze raze b antn/:\:b:where2d x=\:inp}
bounded distinct raze f each .Q.an inter raze inp
// part 2
antn:{(x+/:reverse d),y-/:d:(til count inp)*\:x-y}
f:{distinct raze raze b antn/:\: b:where2d x=\:inp}
bounded distinct raze f each .Q.an inter raze inp