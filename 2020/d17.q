inp:"#"=read0`:day17eg.txt;
inp:"#"=read0`:day17.txt;
// part 1
vectors:`u#({x cross x cross x} -1 0 1) except enlist 0 0 0;
actives:`u#raze {0,'x,\:y}'[where each inp; (til count inp)];
findadj:{`u#vectors +\: x};
iter:{
    map:nb!findadj each nb:`u#distinct x,raze findadj each x;
    map:sum each map in\: x;
    active:`u#(where map in 2 3) inter x;
    inactive:`u#(where map = 3) except x;
    `u#active,inactive
    };
\ts count iter iter iter iter iter iter actives

// part 2
vectors:`u#({x cross x cross x cross x} -1 0 1) except enlist 0 0 0 0;
actives:`u#raze {0 0,/:x,\:y}'[where each inp; (til count inp)];
\ts count iter iter iter iter iter iter actives
// 75s to 1.2s with `u#