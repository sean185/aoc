t:"J"$read0`:day9.txt
// part 1
/ count each -25_ {26 sublist x _ y}[;t] each til count t
mtake:{[w;l] {x sublist y,z}[neg[w];]\[();l]}
p:25_ mtake[26;t]
part1:last first p where not {(last x) in distinct sum each t cross t:25#x} each p

// part 2
part2:{[m;nums]
    nums:nums where nums < m;
    r:2_ til count nums;
    l where m=sum each l:raze mtake[;nums] each r
    }[part1; t]
(min first part2) + (max first part2)

