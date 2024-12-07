// part 1
sum abs (-/)asc each flip "J"$"   "vs/:read0`:d01.txt
// part 2
inp:flip "J"$"   "vs/:read0`:d01.txt
m:desc count each group last inp
sum {x*m[x]}{x where x in key m}first inp