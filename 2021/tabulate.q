\cd C:\Repos\aoc2021
\P 20
json:.j.k first read0 `:474567.json
json:.j.k first read0 `:957756.json
// person
json[`members][`483758][`completion_day_level] 
// person > level
json[`members][`483758][`completion_day_level][`1]
// person > level > star
json[`members][`483758][`completion_day_level][`1][`1]
// person > level > star > ts
json[`members][`483758][`completion_day_level][`1][`1][`get_star_ts]

// {([]star:key x),'value x} json[`members][`483758][`completion_day_level][`1]
// {raze {([]day:x; star:key y),'"P"$string value y}'[key x;x]} json[`members][`483758][`completion_day_level]
tab:(uj/){(`name`id`stars`local_score#x),/: {raze {([]day:x; star:key y),'"P"$string value y}'[key x;x]}x[`completion_day_level] } each value json[`members]
tab:select (`$id)^{$[10h=type x; `$x; `]} each name, day_star:`$((-2#'"0",'string day),'"_",'string star), ts:get_star_ts from tab
P:asc exec distinct day_star from tab
// 0!exec P#(day_star!ts) by name:name from tab
(,'/){
    t:select name, ts from tab where day_star = x;
    n:count[exec distinct name from tab];
    t:`ts xasc n#t,n#enlist `name`ts!(`; ts:0Wp);
    // x xcol select ranking:(name,'`$-10_'string ts) from t
    x xcol select ranking:name from t
    } each P



newday:"25";
system"cd C:/Repos/aoc2021/d",newday;
fs:"d",/:newday,/:(".q";".py";".txt";"eg.txt")
{f:hsym `$x; h:hopen f; hclose h} each fs;
