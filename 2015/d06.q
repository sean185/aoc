inp:read0`:d06.txt
inp:read0`:d06eg.txt
getfn:{(not;1b|;0b&)first where x like/: ("toggle*";"turn on*";"turn off*")}
getinst:{a:" "vs x; start:"J"$","vs first -3#a; end:"J"$","vs last a; (getfn x;start;end)}
insts:getinst each inp
f:{.[x;y[1]+'til each 1+y[2]-y[1];y 0]}
sum raze(1000#enlist 1000#0b)f/insts
// part 2
getfn:{(2+;1+;0|-1+)first where x like/: ("toggle*";"turn on*";"turn off*")}
insts:getinst each inp
sum raze(1000#enlist 1000#0)f/insts
