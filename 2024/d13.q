inp:"J"$","vs/:/:3#'0N 4#inter\:[;"0123456789,"] read0`:d13eg.txt
inp:"J"$","vs/:/:3#'0N 4#inter\:[;"0123456789,"] read0`:d13.txt
// part 1 brute force attempt
sum raze {r:raze ((1+til 100),'x*/:1+til 100){(x[0],y[0];x[1]+y[1];x[2]+y[2])}/:\:(1+til 100),'y*/:1+til 100; w:r where r[;1 2]~\:z; min sum each 3 1*/:w[;0]} ./: inp
// part 2 by manually solving system of linear equations
inp[;2]+:10000000000000
// 94a+22b=8400
// 34a+67b=5400
// ((94*5400)-(8400*34))%(94*67)-22*34
// ((22*5400)-(67*8400))%(22*34)-67*94
f:{
    a:((y[0]*z[1])-(y[1]*z[0]))%(y[0]*x[1])-y[1]*x[0];
    b:((x[0]*z[1])-(z[0]*x[1]))%(x[0]*y[1])-y[0]*x[1];
    (a;b)
 };
chk:{sum raze 3 1*/:`long$x where all flip 0=x mod 1}
chk f ./: inp
// we can also solve using mmu, which is the a game changer for speed to completion
f:{(inv flip (x;y)) mmu z}
chk f ./: `float$inp
