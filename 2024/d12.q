inp:read0`:d12eg.txt
inp:read0`:d12.txt

// prepare by uniquely tagging regions
d:(0 -1;-1 0;0 1;1 0)
where2d:{raze (til count x),/:'where each x} // get 2d coords
g:{raze h each x}/
h:{nb:nb where not null inp ./: nb:x+/:d; nb:nb where null visited ./: nb; c:inp . x; nb:nb where c=inp ./:nb; .[`..visited;;:;visited . x] each nb; nb}
visited:(2#count inp)#0N; while[any raze null visited; p:first where2d null visited; .[`..visited;p;:;0|1+max raze visited]; g enlist p]

// part 1: count adjacent edges in 4 directions only
f:{count raze {(y+/:d)except x}[a;]each a:where2d y=x}
{sum x*f[visited;]each key x} count each group raze visited

// part 2: count the corners
// search clockwise starting from North position:
// inner corners:   count the number of x_x, for a max of 10101010b
//   OXO
//   XXX
//   OXO
// outer corners:   count the number of ___, for a max of 00000000b
//   OOO
//   OXO
//   OOO
// moebius corners: count the number of _x_, for a max of 01010101b
//   XOX
//   OXO
//   XOX
dd:(-1 0;-1 1;0 1;1 1;1 0;1 -1;0 -1;-1 -1)
f2:{sum raze in[;(101b;000b;010b)] @\:[;(0 1 2;2 3 4;4 5 6;6 7 0)] y=x ./:/: dd +\:/: 0N!p:where2d y=x}
{sum x*f2[visited;]each key x} count each group raze visited
