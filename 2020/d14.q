txt:read0`:day14.txt
txt:read0`:day14eg.txt
// part 1
res:()!()
{
    if[x like "mask*";
        m::"J"$'last " " vs x;
        :1b];
    x:" " vs x;
    pos:"J"$1_ -1_ last "mem" vs first x;
    v:"j"$-36#(36#0b),2 vs "J"$last x;
    res[pos]:2 sv 1=v^m
    } each txt
sum value res

// part 2
txt:read0`:day14eg2.txt
findall:{
    {
        $[y[1]="0"; 
            x; 
            y[1]="1";
            x+"j"$2 xexp y[0]; 
            raze x+/:0,"j"$2 xexp y[0]
            ]
        }/[0;flip(reverse til 36;x)]
    }

mask:{{[a;b]$[a="1";a;a="0";b;a]}'[m;x]}
/ m:"000000000000000000000000000000X1001X"
/ mask["000000000000000000000000000000101010"]

res:()!()
{
    if[x like "mask*";
        m::last " " vs x;
        :1b];
    x:" " vs x;
    pos:"J"$1_ -1_ last "mem" vs first x;
    v:"J"$last x;
    res[findall mask raze string -36#(36#0b),2 vs pos]:v
    } each txt

sum raze res