input:"J"$read0 `:day1_input.txt

// part 1
fn:{(floor x%3)-2}
sum fn input

// part 2
fn2:{d:(floor x%3)-2;$[d>0;d;0]}
sum {sum 1_fn2\'[x]} each input
