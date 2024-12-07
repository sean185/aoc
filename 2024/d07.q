inp:": "vs/:read0`:d07.txt
inp:": "vs/:read0`:d07eg.txt
// part 1
sum {y:" "sv reverse" "vs y; b:any (a:"J"$x)=value each @[y;where null y;:;]each (cross/)(sum null y)#enlist"+*"; b*a}./: inp
// part 2 attempt, rewrote but slow
ops:("+",;"*",)
ops:("+",;"*",;"",) 
f:{v:" "vs x; {[x;y](first x){string value x,y}/y@'(1 _x)}[v;]each (cross/)(sum null x)#enlist ops}
sum {("J"$x)*any x~/:f y}./: inp