\cd C:\Repos\aoc2021\d06
fish:count each group value first read0`:d06eg.txt
fish:count each group value first read0`:d06.txt
t:update num:0^fish[age] from ([] age:-1+til 10)
fn:{[tab]
    tab:update num:0^next num from tab;
    add:select age:6 8, 0^2#num from tab where age = -1;
    tab:tab pj 1!add;
    update num:0 from tab where age <0
    };
fn2:{[d]
    d:(-1+key d)!value d;
    d+:6 8!2#0^d[-1];
    d:d _/ k where (k:key d) < 0
    };
// part 1 - 365131
sum 80 fn/t
sum 80 fn2/fish
\ts:1000 sum 80 fn/t // 876 2176
\ts:1000 sum 80 fn2/fish // 234 1312

// part 2 - 1650309278600
sum 256 fn/t
sum 256 fn2/fish
\ts:1000 sum 256 fn/t // 2798 2176
\ts:1000 sum 256 fn2/fish // 750 1344
