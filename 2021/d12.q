\cd C:\Repos\aoc2021\d12
isupper:{upper[x] like x:$[10h=type x; x; string x]}
edges:`src`dest!/:`$"-" vs/: read0 `:d12eg.txt
edges:`src`dest!/:`$"-" vs/: read0 `:d12eg2.txt
edges:`src`dest!/:`$"-" vs/: read0 `:d12eg3.txt
edges:`src`dest!/:`$"-" vs/: read0 `:d12.txt
nodes:update visited:0b, big:isupper each node from ungroup select node:asc distinct (src, dest) from edges

validpaths:{
    // takes in a path, returns a list of paths
    n:last x;
    if[n=`end; :enlist x];
    possible:raze (exec dest from edges where src = n; exec src from edges where dest = n);
    possible:(possible inter exec node from nodes where big),possible except x; // figure out valid nodes
    x,/:distinct possible
    }
paths:enlist enlist `start
count raze validpaths each raze validpaths each raze validpaths each raze validpaths each 
raze validpaths each raze validpaths each raze validpaths each paths
count {raze validpaths each x}/[paths]

// allow visiting exactly one small cave twice
validpaths:{
    // takes in a path, returns a list of paths
    n:last x;
    if[n=`end; :enlist x];
    possible:raze (exec dest from edges where src = n; exec src from edges where dest = n);
    // figure out valid nodes
    possible:$[any 1<(exec node from nodes where not big)#count each group x;
        (possible inter exec node from nodes where big),possible except x;
        possible except `start];
    x,/:distinct possible
    }
count {raze validpaths each x}/[paths]
