\cd C:\Repos\aoc2021\d21
// part 1 - 752745
t:1+til 10; d:1+til 100; p:0; i1:4-1; i2:8-1; s1:0; s2:0; rolls:0; // eg
t:1+til 10; d:1+til 100; p:0; i1:6-1; i2:3-1; s1:0; s2:0; rolls:0; // input
while[not any 1000<=(s1;s2);
    s1+:t (i1+:sum d (p+til 3) mod 100) mod 10; p+:3;
    rolls+:3;
    if[s1>=1000;:1b];
    s2+:t (i2+:sum d (p+til 3) mod 100) mod 10; p+:3;
    rolls+:3;
    if[s2>=1000;:1b]
 ];
rolls*min s1,s2

// part 2 
/ only possibilities of dice: 3 4 5 6 7 8 9!1 3 6 7 6 3 1
count each group sum each {x cross x cross x} 1+til 3
/ we need to track 2 things: current count of positions on the board, and cumulative sums for each possibility
smod:{?[x=10;10;x mod 10]}
rolls:(-1 rotate 1+til 10)!flip smod each (til 10)+/:3+til 7

d:()!();
part2:{[p1;p2;s1;s2;turn]
    k:`$"_"sv string (p1;p2;s1;s2;turn);
    if[k in key d; :d k];
    if[s1>=21;:1 0];
    if[s2>=21;:0 1];
    newkeys:(,'/)$[turn=1;(rolls p1;p2;s1+rolls p1;s2;2);(p1;rolls p2;s1;s2+rolls p2;1)];
    d[k]:res:sum 1 3 6 7 6 3 1*'.z.s ./: newkeys;
    res
 };
part2[4;8;0;0;1]
max part2[6;3;0;0;1]
