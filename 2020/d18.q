// part 1 happens to tbe possible in kdb
weirdmath:{value {leftb:where "("=x; rightb:where ")"=x; @[;leftb;:;")"] @[;rightb;:;"("] x} reverse x}
weirdmath"2 * 3 + (4 * 5)"
weirdmath"5 + (8 * 3 + 9 + 3 * 4 * 3)"
weirdmath"5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
weirdmath"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
sum weirdmath each read0`:day18.txt

// part 2 not so.