inp:raze read0`:d03.txt
// part 1
inp:"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
f:{sum {x*y}.'{x where all each not null x}"J"$","vs/:first each ")" vs/: "mul(" vs x}
f inp
// part 2
inp:"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
f2:{sum f each first each "don't()" vs/: "do()" vs x}
f2 inp
