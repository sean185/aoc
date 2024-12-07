\cd C:\Repos\aoc2021\d09
// part 1
m:(-1 0;1 0;0 -1;0 1)
g:"J"$''read0 `:d09.txt
g:"J"$''read0 `:d09eg.txt
p:(til x:count g) cross (til y:count first g)
sum 1+{g[x;y]} ./: p where {l:{g[x;y]} ./: m+\:x; l:l where not null l; all l>g[x[0];x[1]]} each p

// part 2
m:(-1 0;1 0;0 0;0 -1;0 1)
fn:{[grid;pts] res:grid ./: pos:raze m +\:/:pts; asc distinct pos where (not null res) and (res < 9)}
f:fn[g;]
prd 3#desc {[g]
    sizes:();
    while[sum 9>raze g;
        // pick a cluster and find all nearby
        p:(til count g) cross (til count first g);
        seed:first p where 9>g ./: p;
        f:fn[g;];
        sizes,:count cluster:f/[enlist seed];
        // delete cluster after
        g:.[;;:;9]/[g;cluster]
    ];
    sizes
 }[g]
