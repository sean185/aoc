map:read0`:d16.txt
map:read0`:d16eg.txt
NESW:(-1 0;0 1;1 0;0 -1)
actions:({@[x;0 1;+;NESW x 2],1};{@[x;2;{(x+1)mod 4}],1000};{@[x;2;{(x-1)mod 4}],1000})
where2d:{raze (til count x),/:'where each x} // get 2d coords
initial:(first where2d map="S"),1
final:(first where2d map="E")
print:{map .[;;:;"R"]/ distinct (key x)[;0 1]}
visited:(enlist initial)!enlist 0
// x, y, dir, dweight, tweight
// for each iteration, consider paths which have lower cumulative weights
f:{np:raze (actions@/:\:x),'\:0^visited@x; np:np where not"#"=map ./:np[;0 1]; rem:np where (not np[;0 1 2] in key visited) or (s:np[;3]+np[;4])<visited np[;0 1 2]; visited&:np[;0 1 2]!s;  distinct rem[;0 1 2]}
f/[enlist initial]
score:min visited final,/:til 4
// part 2 - tip from u/aadi312 to only backtrack using 1 (step) or 1001 (turn and step)
goal:where visited=score
g:{np where (v in visited[x]-1 1001) and not null v:visited np:(x[0 1]+/:NESW),'2 3 0 1} // reverse directions to backtrack
pos:raze {distinct raze g each x}\[-1#goal]
count distinct pos[;0 1]
-1 {.[;;:;]/[map;x[;0 1];"^>v<"x[;2]]} pos
