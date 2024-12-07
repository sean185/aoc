t:{(`$x[0];"J"$x[1])} each " " vs/: read0`:day8.txt;
// part 1
fn:{[t]
    pos:0; acc:0; executed:();
    while[(not exitflag:pos in executed) and pos<count t;
        / 0N!(pos;acc;t[pos]);
        ins:t[pos]; executed,:pos;
        $[
            ins[0]=`acc; [acc+:ins[1]; pos+:1];
            ins[0]=`jmp; pos+:ins[1];
            pos+:1]
        ];
    (exitflag;pos;acc;executed)
    };

0N!fn[t];

// part 2
possibilities:{
    tmp:t; ins:tmp[x];
    ins[0]:(`nop`jmp!`jmp`nop)ins[0];
    tmp[x]:ins;
    tmp
    } each where (t@'0) in `nop`jmp;

result:{0N!x; fn[y][0 1 2]}'[where (t@'0) in `nop`jmp;possibilities]
result[where not result@'0]