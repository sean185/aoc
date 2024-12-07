// my first stab
parser:{
    t:trim each "," vs x;
    t:(trim each "contain" vs t[0]),1_ t;
    p:" " sv 2# " " vs t[0];
    c:count components:{qty:"J"$x[0];name:`$" " sv x[1 2];$[null qty;(0N;`);(qty;name)]} each " " vs/: 1_ t;
    colnames:raze `p,{t:"c",string 1+x;`$(t,"q";t)} each til c;
    :colnames!(`$p),raze components;
    }
// part 1
t:(uj/) enlist each parser each read0`:day7eg.txt
t:(uj/) enlist each parser each read0`:day7.txt
b:`$"shiny gold"
asc distinct raze 1_ -1_ {[matchlist] exec p from t where (c1 in matchlist) or (c2 in matchlist) or (c3 in matchlist) or (c4 in matchlist)}\[1#b]
// part 2
res:{[d] 
    // result:select matchlist:(c1,c2) except `, qty:(c1q,c2q) except 0N by p from t where p in (key d);
    result:select matchlist:(c1,c2,c3,c4) except `, qty:(c1q,c2q,c3q,c4q) except 0N by p from t where p in (key d);
    result:exec matchlist, qty:d[p]*qty from result;
    ((raze result[`matchlist])!raze result[`qty])
    }\[(1#b)!(1#1)]
sum raze value each 1_ -1_ res


// revised solution
parser:{raze {p:`$"" sv 2# " " vs x[0]; `parent`weight`child!/:p,/:{l:" " vs x; qty:"J"$l[0]; $[null qty;(qty;`);(qty;`$"" sv l[1 2])] } each ", " vs x[1]} each " contain " vs/: x}
t:parser read0`:day7eg.txt
t:parser read0`:day7.txt
// part 1
count distinct raze 1_ -1_ {[matchlist] exec distinct parent from t where child in matchlist}\[1#`shinygold]
// part 2
sum raze value each 1_ -1_ {[d] r:exec child!d[parent]*weight from t where parent in (key d), not null child}\[(1#`shinygold)!(1#1)]
