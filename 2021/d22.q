\cd C:\Repos\aoc2021\d22
range:{x + til 1+y-x};
parseline:{
    x:" " vs x;
    onoff:"on"~first x;
    xyz:"J"$".."vs/:2_/:"," vs last x;
    `onoff`xr`yr`zr!(enlist onoff),xyz
 };
tab:parseline each 20#read0`:d22eg.txt
/ part 1 - 
tab:parseline each 20#read0`:d22.txt
part1:{coords:(range . y`xr) cross (range . y`yr) cross (range . y`zr); $[y`onoff;distinct x,coords;distinct x except coords]}
count part1/[();tab]

/ part 2 - 
tab:parseline each read0`:d22eg2.txt
rinter:{x:asc x; y:asc y; if[(max[x]<min[y]) or (max[y]<min[x]); :()]; (max(x 0;y 0);min(x 1;y 1))}
cinter:{[c1;c2] rinter ./: flip(c1;c2)}
cinter . ((-20 26;-36 17;-47 7);(-20 33;-21 23;-26 28))
{cinter'[y[`xr`yr`zr]}/[();tab]
{x,y}\[til count tab]
/ accumulate what needs to be on or off as multiple cuboids
/ if on cube, remove diff from the cumulative, keep cube + remaining pieces
/ if off cube, remove diff from the cumulative, keep remaining pieces
ons:select cube1:flip (xr;yr;zr) from tab where onoff
offs:select cube2:flip (xr;yr;zr) from tab where not onoff
update subtract:cinter ./: cube

[(0 1;0 1)] add (1 2;1 2) --> [(0 0;0 0);(0 1;0 1);(1 0;1 0);(1 2;1 2)]
[(0 1;0 1)] sub (1 2;1 2) --> [(0 0;0 0);(0 1;0 1);(1 0;1 0)]
cinter:{[c1;c2] overlap:rinter ./: flip(c1;c2); c1[0]}
cinter[(0 1;0 1);(1 2;1 2)]
// top, bottom, left, right, topleft, topright, botleft, botright, center
split:{[c1;c2]
    :disp:c2[;0]-c1[;0];
    (c1[;0];c1[;1]-c2[;0]); // top left
    (c1[;0];c1[;1]-c2[;0]) // top 
    }
split[(0 1;0 1);(1 1;1 1)]
split[(0 1;0 1);(1 1;0 1)]
split[(1 1;0 1);(0 1;0 1)]
(0 1;0 1)[;1]