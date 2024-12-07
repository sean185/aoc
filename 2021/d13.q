\cd C:\Repos\aoc2021\d13
tmp:"\n\n" vs "\n" sv read0 `:d13eg.txt;
tmp:"\n\n" vs "\n" sv read0 `:d13.txt;
tab:`x`y!/:points:value each "\n" vs tmp[0];
inst:{(`$x[0];"J"$x[1])} each "=" vs/: last each " " vs/: "\n" vs tmp[1];

fold:{[tab;ins]
    ax:ins[0]; pos:ins[1];
    ![tab;enlist(>;ax;pos);0b;(1#ax)!enlist({x-2*x-y};ax;pos)]
 }

// part 1
count distinct fold[tab;first inst]
// part 2
plot:{g:{y#enlist x}/[".";1+max each x`x`y]; .[;;:;"#"]/[g;flip x[`y`x]]}
plot fold/[tab;inst]