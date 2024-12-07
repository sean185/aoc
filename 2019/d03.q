instructions:("U7,R6,D4,L4";"R8,U5,L5,D3") // 6 - ok
instructions:("R75,D30,R83,U83,L12,D49,R71,U7,L72";"U62,R66,U55,R34,D71,R55,D58,R83") // 159 - ok
instructions:("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51";"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") // 135 - ok
instructions:read0 `:day3_input.txt

// part 1 
// x-y grid reference
traverse:{[pos;inst]
    ref:last pos;
    d:first inst;
    m:"J"$1_inst;
    npos:1_ $[
        d="U";ref[0] cross ref[1]+til 1+m;
        d="D";ref[0] cross ref[1]-til 1+m;
        d="L";(ref[0]-til 1+m) cross ref[1];
        d="R";(ref[0]+til 1+m) cross ref[1];
    '`err];
    pos,npos
    };

paths:traverse/[enlist 0 0; ] each "," vs' instructions;

findclosest:{[paths]
    t:([]ip:paths[0] inter paths[1]);
    t:select m:sum each abs each ip from t;
    exec min m from t where m > 0
    };

\t:10 findclosest[paths] // 529ms per trial


// part 1 alt
part1:{
    inp:"," vs'read0 `:day3_input.txt;
    d:"UDLR"!(0 1;0 -1;-1 0;1 0);
    p:{(+\) raze ("J"$1_'x)#'d[1#'x]} each inp;
    min sum each abs each inter/[p]
}
\t:10 part1[] // 53ms per trial


// part 2
findshortest:{[paths]
    t:([]ip:paths[0] inter paths[1]);
    t:update L:(paths[0] ?/: ip), R:(paths[1] ?/: ip) from t;
    t:update s:L+R from t;
    exec min s from t where s > 0
    };
findshortest[paths] // 20386
