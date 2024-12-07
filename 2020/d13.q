t:read0`:day13eg.txt
t:read0`:day13.txt

c:"J"$t[0]
buses:("J"$csv vs t[1]) except 0N
// part 1
m*first buses where times=m:min times:buses - c mod/: buses

// part 2
buses:"J"$csv vs t[1]
/ buses:"J"$csv vs "67,7,x,59,61"
/ buses:"J"$csv vs "1789,37,47,1889"
b:buses where not null buses
c:(til count buses) where not null buses

findlcm:{[ab;d]
    ab*{[ab;d;nm]
        r:(d;0)+ab*nm;
        if[r[0]=r[1];
            :nm];
        $[r[0] > r[1];
            (nm[0];nm[1]+1|floor(r[0]-r[1])%ab[1]); // optimizes for b assuming a is always far larger
            (nm[0]+1;nm[1])
            ]
        }[ab;d;]/[1 1]
    };

// some "base case"
findlcm[3 5;1]
findlcm[5 8;1]

// working through example
findlcm[7 13;1]
findlcm[(7*13;59);3+78]
findlcm[(7*13*59;31);2+354]
findlcm[(7*13*59*31;19);1+70153]

// putting it all together
(neg last c)+last {0N!(x[0]*y[0]; last findlcm[x[0],y[0];x[1]+y[1]])}/[(1 0);flip (b;deltas c)]
