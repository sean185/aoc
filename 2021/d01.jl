fn = "d01eg.txt"
fn = "d01.txt"
l = map(x -> parse(Int, x), readlines(fn))

part1(l) = sum(map( x -> x[1]<x[2], zip(l[1:end-1],l[2:end])))
@time part1(l)
@time part1(l)

part2(l) = part1(map(x -> sum(x), zip(l[1:end-2],l[2:end-1],l[3:end])))
@time part2(l)
@time part2(l)
