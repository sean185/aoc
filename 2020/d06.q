t:read0`:day6.txt
tbl:([]"  " vs " " sv t)
// part 1
exec sum {count .Q.a inter x} each chars from tbl
// part 2
exec sum {count (inter/)" " vs x} each t from tbl