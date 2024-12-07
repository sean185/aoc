inp:"J"$3 5#/:read0`:d03.txt
// part 1
sum {last[x]<sum 2#x:asc x} each inp
// part 2
sum {last[x]<sum 2#x:asc x} each 0N 3#raze flip inp
