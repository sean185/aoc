\cd C:\Repos\aoc2021\d15
map:"J"$'' read0 `:d15eg.txt;
map:"J"$'' read0 `:d15.txt;
dist:c#enlist (c:count map)#0W;
dist[0;0]:0;
visited:c#enlist (c:count map)#0b;

getnbs:{[m;p] d:(1 0; 0 1; -1 0; 0 -1);nb where {all y within 0,x}[-1+count m] each nb:p+/:d}

// part 1 - 435
visit1:{[node; dist; visited]
    nbs:nbs where not visited ./: nbs:getnbs[map;node];
    updist:(dist . node) + map ./: nbs;
    cmpdist:dist ./: nbs;
    dist:.[;;:;]/[dist;nbs;min(updist; cmpdist)];
    visited:.[visited;node;:;1b];
    (nbs;dist;visited) // where updist = min updist
 };
/ visit1[0 0;dist;visited]

pt1:{[ndv]
    nodes:ndv[0]; dist:ndv[1]; visited:ndv[2];
    if[(0W>last last dist) or (0=count nodes);:ndv];
    newstate:visit1[nodes[0]; dist; visited];
    nbs:newstate[0]; dist:newstate[1]; visited:newstate[2];
    newnodes:distinct newnodes iasc dist ./: newnodes:(1_ nodes),nbs;
    / newnodes:newnodes where not visited ./: newnodes;
    (newnodes; dist; visited)
 };

\ts last last @[;1] pt1/[(enlist 0 0;dist;visited)]


// part 2 - 2842
map:"J"$'' read0 `:d15eg.txt;
map:"J"$'' read0 `:d15.txt;
map:(smod[;9]'') raze (,'/) each {map + x}''[(til 5)+/:\:(til 5)]
dist:c#enlist (c:count map)#0W;
dist[0;0]:0;
visited:c#enlist (c:count map)#0b;

smod:{$[x>y;x-y*x div y;x]}
\ts last last @[;1] pt1/[(enlist 0 0;dist;visited)]
