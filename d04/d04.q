inp:read0`:d04.txt
inp:read0`:d04eg.txt
// part 1
d:((0 0;0 1;0 2;0 3);(0 0;1 0;2 0;3 0);(0 0;1 1;2 2;3 3);(0 3;1 2;2 1;3 0))
count {x where any x like/: ("XMAS";"SAMX")}raze inp ./:/:/: d +\:\:/:{x cross x}til count inp
// part 2
d:(-1 -1;1 1;0 0;-1 1;1 -1)
count {x where any x like/:("MSAMS";"SMAMS";"MSASM";"SMASM")}inp ./:/: d +\:/:{x cross x}til count inp

