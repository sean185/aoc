// bfs to generate mappings
d:(1 0;-1 0;0 1;0 -1)
dpad:"^A<v>"!(0 1;0 2;1 0;1 1;1 2) 
npad:"7894561230A"!(0 0;0 1;0 2;1 0;1 1;1 2;2 0;2 1;2 2;3 1;3 2)
bfs:{[m;dst;paths] if[any b:dst in/:paths;:paths where b]; distinct raze paths{$[y in x;x;x,enlist y]}/:'np@' where each in[;m] np:d+\:/:last each paths };
nmap:{x!{{,[;"A"]1_"v^><"d ? deltas x}each bfs[npad;y]/[enlist enlist x] } ./: npad x} {x cross x} "7894561230A"
dmap:{x!{{,[;"A"]1_"v^><"d ? deltas x}each bfs[dpad;y]/[enlist enlist x] } ./: dpad x} {x cross x} "^A<v>"
final:{min count each x}each 
    {x where c=min c:count each x}each raze each {({(cross/)dmap "A"^prev[x],'x}'')x}
    {x where c=min c:count each x}each raze each {({(cross/)dmap "A"^prev[x],'x}'')x}nmap
sum {("J"$x inter .Q.n)*sum final"A"^prev[x],'x}each read0`:d21.txt

// part 2
/ 4 pads -> 3 transitions
/ 27 pads -> 26 transitions
resmap:{min count each x}each dmap // me
do[24;resmap:{min {sum resmap "A"^prev[x],'x}each x} each dmap] // n-3
resmap:{min {sum resmap "A"^prev[x],'x}each x} each nmap // robot
sum {("J"$x inter .Q.n)*sum resmap"A"^prev[x],'x}each read0`:d21.txt
