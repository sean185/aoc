\cd C:\Repos\aoc2021\d24
parser:{$[x[0] in ("div";"mod"); @[x;0;:;x[0],"2"]; x]}
ins:parser each " " vs/: read0 `:d24eg.txt
ins:parser each " " vs/: read0 `:d24eg2.txt
ins:parser each " " vs/: read0 `:d24eg3.txt
ins:parser each " " vs/: read0 `:d24.txt


part1:{[state;i]
    cum:state; 
    p:`w`x`y`z?`$i[1];
    if[i[0]~"inp";
        cum:0N!raze (1+til 9){x,y,x}\:/:1_' cum;
        0N!count cum
        / cum[p]:"J"$first num;
        / num:1_ num;
        ];
    v:$[first i[2] in "wxyz"; cum `w`x`y`z?`$i[2]; "J"$i[2]];
    if[i[0]~"add";
        cum[p]+:v
        ];
    if[i[0]~"mul";
        cum[p]*:v
        ];
    if[i[0]~"eql";
        cum[p]:0+cum[p]=v
        ];
    if[i[0]~"div";
        cum[p]:floor cum[p]%v
        ];
    if[i[0]~"mod";
        cum[p]:cum[p] mod v
        ];
    t:0!select max num by z from ([]z:first each 3_' cum; num:4_'cum)
    distinct 0 0 0,/: 3_'cum
 };

/ part1/[(0 0 0 0;1#"1"); " " vs/: read0 `:d24eg.txt]
/ part1/[(0 0 0 0;"13"); " " vs/: read0 `:d24eg2.txt]
/ part1/[(0 0 0 0;1#"9"); " " vs/: read0 `:d24eg3.txt]
/ part1/[(0 0 0 0;"13579246899999"); " " vs/: read0 `:d24.txt]
res:part1/[enlist 0 0 0 0;" " vs/: read0 `:d24.txt]
res where 0=last each res
{part1/[enlist 0 0 0 0;x]} each 0N 14 #" " vs/: read0 `:d24.txt
0N 18 #read0 `:d24.txt
\
inp:{(`$x) set "J"$first num; `num set 1 rotate num};
add:{a:`$x; b:value y; a set b + value a};
mul:{a:`$x; b:value y; a set b * value a};
eql:{a:`$x; b:value y; a set "J"$b=value a};
div2:{a:`$x; b:value y; a set floor (value a)%b};
mod2:{a:`$x; b:value y; a set (value a) mod b};
{[i] value i; 0N!(w;x;y;z)} each ins
(w;x;y;z)
1 0 0 1
num:"99999999999999";w:x:y:z:0;
i:0;
while[1b;
    / 0N!num;
    w:x:y:z:0;
    value each ins;
    if[z=0; 0N!(w;x;y;z);];
    i+:1;
    num:string 99999999999999-i;
    while["0" in num;
        i+:1;
        num:string 99999999999999-i];
 ]
