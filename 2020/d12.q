t:{(`$1#x;"J"$1_x)} each read0 `:day12eg.txt
t:{(`$1#x;"J"$1_x)} each read0 `:day12.txt

bearings:`N`E`S`W
dirs:(0 1;1 0;0 -1;-1 0) // NESW
rot:{[inst;ort]
    // inst is the instruction to rotate i.e. (`R;90)
    // ort is the current orientation i.e. bearings
    // returns new orientation i.e. bearings
    first ((-1 1 inst[0]=`R)*"j"$inst[1]%90) rotate (bearings?ort) rotate bearings
    };

// part 1
part1:{[state;inst]
    (state; inst);
    if[inst[0] in bearings;
        state[`position]+:inst[1]*dirs (bearings ? inst[0])
        ];
    if[inst[0] in `L`R;
        state[`bearing]:rot[inst;state[`bearing]]
        ];
    if[inst[0] = `F;
        state[`position]+:inst[1]*dirs (bearings ? state[`bearing])
        ];
    state
    };

res1:part1/[`bearing`position!(`E;0 0);t]
sum abs res1[`position]

// part 2
/ start -> 10 1
/ rot R -> 1 -10
/ rot R -> -10 -1
rotw:{[inst;waypoint]
    // inst is the instruction to rotate i.e. (`R;90)
    // waypoint is the coordinates of the waypoint relative to the ship
    // returns new waypoint relative coordinates
    d:$[inst[0]=`R; (0 -1f;1 0f); (0 1f;-1 0f)]; // right and left rotation matrix
    "j"$("f"$waypoint)mmu(mmu/)("j"$inst[1]%90)#enlist d
    }
/ rotw[(`R;90);10 1]
/ rotw[(`L;90);10 1]

part2:{[state;inst]
    (state; inst);
    if[inst[0] in bearings;
        state[`waypoint]+:inst[1]*dirs (bearings ? inst[0])
        ];
    if[inst[0] in `L`R;
        state[`waypoint]:rotw[inst;state[`waypoint]]
        ];
    if[inst[0] = `F;
        state[`position]+:inst[1]*state[`waypoint]
        ];
    state
    };

res2:part2/[`waypoint`position!(10 1;0 0);t]
sum abs res2[`position]
