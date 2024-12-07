sep:0,where ""~/:t:read0`:day16.txt;
sep:0,where ""~/:t:read0`:day16eg.txt;
sep:0,where ""~/:t:read0`:day16eg2.txt;
validations:{x:": " vs x; k:`$x[0]; `k`r1`r2!(enlist k),"J"$ "-" vs/: " or " vs x[1]} each sep[0]_sep[1]#t;
c:count validations;
myticket:(c#"J";csv) 0: 2_sep[1]_sep[2]#t;
data:(c#"J";csv) 0: 2_sep[2]_t;

// part 1 - find values which fail every validation possible
search:distinct asc raze value exec raze {x[0]_til 1+x[1]} each r1, raze {x[0]_til 1+x[1]} each r2 from validations
sum raze {raze x where not x in search} each data

// part 2
fields:flip (flip data) where not any {not x in search} each data
t:update v:{[cl;v] where all each (cl within v[0]) or (cl within v[1])}[fields] each flip (r1;r2) from validations
t:update v except' prev v from `c xasc update c: count each v from t
idx:exec first each v from t where k like "departure*"
prd (first flip myticket)[idx]