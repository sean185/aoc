input:"J"$"," vs first read0 `:day2_input.txt

// part 1
input[1]:12
input[2]:2
first {$[
    y[x]=1;[ y[y[x+3]]:sum y@y@x+1 2; .z.s[x+4;y] ];
    y[x]=2;[ y[y[x+3]]:prd y@y@x+1 2; .z.s[x+4;y] ];
    y[x]=99;y;
    '"err!"]}[0;input]

// part 2
fn:{$[
    y[x]=1;[ y[y[x+3]]:sum y@y@x+1 2; .z.s[x+4;y] ];
    y[x]=2;[ y[y[x+3]]:prd y@y@x+1 2; .z.s[x+4;y] ];
    y[x]=99;y;
    '"err!"]}


// part 1 alt
TEST:{
    p:x[0]; c:x[1]; op:c@p;
    if[op=99; :x];
    ops:1 2!(sum;prd);
    c[c@p+3]:ops[op] c@c@p+1 2;
    :(p+4;c)
    }/;

intcodes:"J"$"," vs first read0 `:day2_input.txt
intcodes[1 2]:12 2
TEST (0;intcodes)




// unfortunate bruteforce search
update first each fn[0;] each inp from 
update inp:{@[x;1 2;:;y]}[input;] each n from
select n:n cross 92 from ([]n:til 120)
// answer! 38 92

