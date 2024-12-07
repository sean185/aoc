\cd C:\Repos\aoc2021\d11
t:"J"$''read0 `:d11eg.txt
t:"J"$''read0 `:d11.txt
dirs:{x except enlist 0 0} {x cross x } -1 0 1 

/ inc all by 1
/ for each that have 9, flash, return to 0, and stay there
/ for each that are adjacent, if new, also increase by 1
/ for all that flashed, set to 0N, then set to 0 // x ./: raze coords +/:\: dirs
flash:{[g]
    h:til count g;
    v:til count first g;
    coords:h cross v;
    affected:coords where 9< g ./: coords;
    g:.[;;:;0N]/[g;affected];
    g:.[;;+;1]/[g;(raze affected +/:\: dirs) inter coords];
    g
    };

// part 1 - 1585
{[g;n]
    flashes:0;
    i:0;
    do[n;
        g+:1; i+:1;
        g:0^flash/[g];
        flashes+:count where isit:0=raze g
        ];
    flashes
 }[t;100]

// part 2 - 382
// just... search until error
{[g;n]
    flashes:0;
    i:0;
    do[n;
        g+:1; i+:1;
        g:0^flash/[g];
        flashes+:count where isit:0=raze g;
        if[all isit; 'string i]
        ];
    flashes
 }[t;2000]


