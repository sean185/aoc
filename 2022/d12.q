// do a bfs from goal back
heights:"S",.Q.a,"E"
dulr:(1 0;-1 0;0 1;0 -1)
f:`:d12eg.txt
f:`:d12.txt
topo:heights?read0 f
find:{raze (til count topo),/:'where each (heights?x)=topo}

// find valid paths from one path
fn:{
    curr:last x;
    diffs:(topo . curr)-p:topo ./: branches:curr+/:dulr; 
    branches:branches where (&/)(diffs <=1;not null diffs;not branches in touched);
    touched,:branches;
    x,/:enlist each branches
    }

// do a BFS from the goal backwards
run:{
    start::find "E";
    end::x;
    touched::start;
    allpaths::([]path:enlist start);
    while[0=count select from allpaths where any each end in/: path; // return because found!
        allpaths::ungroup select fn each path from allpaths];
    min exec -1+count each path from select path from allpaths where any each end in/:path
    }

// part 1
run find "S"

// part 2, any path will do!
run find "a"

/2162 12752
\ts:10 run find "S"
/5576 168368
\ts:10 run find "a"

v2:

where2d:{raze(til count x),/:'where each x}
adj:{(1 0;-1 0;0 1;0 -1)+\:x}
{new:{vals:topo ./: nbs:adj x; nbs where (&/)(-1<=vals-topo . x;not null vals)} each where2d {x=max each x} x;x .[;;:;0]/new}0N 0@27=topo

// visited and scores