inp:read0`:d02.txt
inp:read0`:d02eg.txt
// part 1
np:","vs"123,456,789"
d:"UDLR"!(-1 0;1 0;0 -1;0 1)
f:{[p;ins] p{$[null np . x+y;x;x+y]}/ins}
np ./: 1 1 f\d inp
// part 2
np:","vs"  1  , 234 ,56789, ABC ,  D  "
np ./: 2 0 f\d inp
