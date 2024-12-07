\cd C:\Repos\aoc2021\d10
txt:read0 `:d10.txt
txt:read0 `:d10eg.txt
opening:"<{[("
closing:">}])"
pts:closing!reverse 3 57 1197 25137
// part 1 - 399153
fn:{
    $[y in opening;
        x,y;
        y=(opening!closing)last x;
        -1_ x;
        '1#y
        ]
    }
sum pts raze {x where 1=count each x} @[fn/["";];;0N!] each txt

// part 2 - 2995077699
pt2:t where not 1=count each t:@[fn/["";];;0N!] each txt
scoring:" )]}>"
`long$med {{y+5*x}/[x]} each scoring?reverse each (opening!closing)pt2