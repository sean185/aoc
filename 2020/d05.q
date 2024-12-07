txt:read0`:day5.txt
// tests
2 sv "B"="BFFFBBF"
2 sv "B"="FFFBBBF"
2 sv "R"="RRR"
{(8*2 sv "B"=7#x)+(2 sv "R"=-3#x)} each ("FBFBBFFRLR";"BFFFBBFRRR";"FFFBBBFRRR";"BBFFBBFRLL")
// part 1
t:`id xdesc update id:col+8*row from {`row`col!(2 sv "B"=7#x;2 sv "R"=-3#x)} each txt
// part 2
exec (til max id) except id from t
