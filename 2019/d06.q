edges:`src`dest!/:`$")"vs'read0`:day6_sample.txt
edges:`src`dest!/:`$")"vs'read0`:day6_sample2.txt
edges:`src`dest!/:`$")"vs'read0`:day6_input.txt
edges:update `u#dest from edges

// part 1
locate:{[p]
    s:exec first src from edges where dest=p[`node];
    if[not s=`; p[`node]:s; p[`dist]+:1];
    p
    }/
    
// 1475ms --> 546ms after applying `u# on dest
\t exec sum dist from locate each select node:dest, dist:0 from edges 


// part 2
transfer:{[paths]
    if[any t:`YOU`SAN~/:{(first x; last x)} each paths; :paths where t];
    raze {
        t:last x; // search for possible continuations
        np:raze (exec dest from edges where src=t),(exec src from edges where dest=t);
        np:np except x;
        $[count np; x,/:np; ()] // return nothing when there's no more traversal possible
        } each paths where not paths ~\: ()
    }/

paths:enlist 1#`YOU
\t -3+count each transfer paths // 19ms --> 8ms after `u attribute
