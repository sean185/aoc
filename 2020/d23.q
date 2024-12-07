input:"J"$'"389125467";
input:"J"$'"589174263";
cups:{l:(1+count x)#0N; @[l;x;:;1 rotate x]}input;
start:first input;
part1:{[n; cup; input]
    do[n;
        grabbed:input\[3;cup];
        nextcup:input grabbed 3;
        / find destcup
/         possibles:({x where x >0} cup - 1+til 5) except grabbed;
/         destcup:0N!$[0=count possibles; max ((count input)-1+til 4) except grabbed; max possibles];
        destcup:cup-1; find:1b;
        while[find;
            $[(not destcup in grabbed) and destcup > 0; 
                find:0b;
                destcup-:1];
            if[destcup<=0; destcup:(count input)-1]
            ];
        input[(grabbed 3; destcup; cup)]:(input destcup; grabbed 1; nextcup);
        cup:nextcup
        ];
    input
    };
    
\ts res:part1[100;start;cups]
res\[8;1]

// part 2
cups:`u#{l:(1+count x)#0N; @[l;x;:;1 rotate x]}input,(count input)_1+til 1000000;
\ts res:part1[100000;start;cups]
/ 18940 8389344
prd res\[2;1]


