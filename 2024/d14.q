bound:11 7; fn:`:d14eg.txt
bound:101 103; fn:`:d14.txt
inp:`p`v!/:(get'')" "vs'inter\:[;.Q.n,"- ,"] read0 fn
print:{-1""; -1 flip (bound#".") .[;;:;"o"]/x[`p]; x}
// part 1
f:{[x;y] update p:(p+y*v)mod'\:bound from x}
chk:{select count i by b:p<\:1+bound div 2 from x where not any each p=\:bound div 2} 
prd chk f[inp;100]
// part 2
{res:f[inp;x]; if[count[inp]=count distinct res[`p]; 'string x];} each 100+til 100000
print f[inp;6668]
\c 105 105