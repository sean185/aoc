inp:"J"$''read0`:d10eg.txt
inp:"J"$''read0`:d10.txt
where2d:{raze (til count x),/:'where each x} // get 2d coords
d:(1 0;0 1;-1 0;0 -1)
f:{v:inp . first x; if[v=9; :x]; distinct np where (v+1)=inp ./: np:raze d+\:/:x}
f:{v:inp . first x; if[v=9; :x]; np where (v+1)=inp ./: np:raze d+\:/:x} // part 2!
sum {count f/[enlist x]}each where2d 0=inp
