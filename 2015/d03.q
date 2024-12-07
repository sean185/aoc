inp:first read0`:d03.txt
// part 1
m:"^v<>"!(0 1;0 -1;-1 0;1 0)
count distinct (+\)(enlist 0 0),m inp
// part 2
count distinct raze {(+\)(enlist 0 0),m x}each flip 0N 2#inp