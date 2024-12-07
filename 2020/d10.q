t:([]j:{0,x,3+max x} asc "J"$read0`:day10eg1.txt)
t:([]j:{0,x,3+max x} asc "J"$read0`:day10eg2.txt)
t:([]j:{0,x,3+max x} asc "J"$read0`:day10.txt)

// part 1
exec prd value count each group deltas j from t

// part 2 - build a list of nodes which are within dist=3, then cascade the from leaf to root
{
    tmp:select j, p:{[x;y] 1_ l where l <= 3+first l:x _ y}[;j] each i from t;
    tmp:update c:1, p:enlist j from tmp where j=max j;
    {update c:sum each (j!c)p from x}/[tmp]
    }[]

// timed runs with \ts:100
// eg1 - 12 9600
// eg2 - 33 9792
// act - 310 20128

