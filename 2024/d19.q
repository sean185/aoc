// part 1 - search down and fork
txt:read0`:d19.txt
txt:read0`:d19eg.txt
towels:", " vs first txt
combis:2_txt
f:{[towels;word;state]
    pos:state 0; possb:state 1;
    if[0=count possb;:state]; // base case
    if[word in possb;:(pos;enlist word)]; // found!
    if[all (count each possb)>=count word;:(pos;())]; // nothing else to search
    a:possb where (count each possb)<=pos; // to extend
    b:possb except a; // to pass on 
    c:distinct b,raze a,/:\:towels where (first each towels)=word pos;
    (pos+1;c where word like/:(c,'"*"))
 }
sum {count last f[towels;x]/[(0;enlist"")]} each combis

// part 2 - use a dict!
f:{[towels;word;state]
    pos:state 0; possb:state 1;
    if[all word ~/: possb`p;:state]; // found!
    a:select p:(p,'t), c from ([]t:towels where towels[;0]=word pos) cross select from possb where (count each p)<=pos; // to extend
    b:select from possb where (count each p)>pos;
    c:0!select sum c by p from (a,b);
    (pos+1;select from c where word like/:(p,'"*"))
 }
sum {exec first c from last f[towels;x]/[(0;([]p:enlist""; c:enlist 1))]} each combis
