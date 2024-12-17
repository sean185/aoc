// part 1
xor:{v:2 vs/:(x;y);c:max count each v;if[c=0;:0]; 2 sv (<>).(neg c)#'(c#0),/:v}
f:{[prog;iro]
    i:iro[0]; r:iro[1]; o:iro[2]; op:prog i; opr:prog i+1; cb:$[4>opr;opr;r[opr-4]];
    if[i>=count prog;:iro]; // halting condition
    $[op in 0 6 7;[r[0 6 7?op]:r[0]div 2 xexp cb; i+:2]; 
      op=1;[r[1]:xor[r[1];opr]; i+:2];
      op=2;[r[1]:cb mod 8; i+:2];
      op=3;$[0<>r[0];i:opr;i+:2];
      op=4;[r[1]:xor . r 1 2;i+:2];
      op=5;[o,:cb mod 8; i+:2];
      '"invalid"];
    (i;r;o)
 };
g:{f[y]/[(0;x;())]}
g[0 0 9;2 6]
g[10 0 0;5 0 5 1 5 4]
g[2024 0 0;0 1 5 4 3 0]
g[0 29 0;1 7]
g[0 2024 43690;4 0]
","sv string last g[729 0 0;0 1 5 4 3 0]
","sv string last g[23999685 0 0;2 4 1 1 7 5 1 5 0 3 4 4 5 5 3 0] // actual

// part 2
g[117440 0 0;0 3 5 4 3 0]
// left most octal undergoes a map to become right most octal
h:{last g[x,0 0;2 4 1 1 7 5 1 5 0 3 4 4 5 5 3 0]}
// uh oh, there may be multiple possibilities! fml.
min 8 sv'(enlist()){raze x,/:'l:{where y=first each h each x}[;y]each 8 sv/:/: x,/:\:til 8}/reverse 2 4 1 1 7 5 1 5 0 3 4 4 5 5 3 0
