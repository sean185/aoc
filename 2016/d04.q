inp:{x:"["vs -1_ x;a:"-"vs x[0];("-"sv -1_a;"J"$last a;x 1)}each read0`:d04.txt
// part 1
sum {x[;1]} inp where {x[2]~5#key desc count each group asc x[0] except "-"} each inp
// part 2
{x where x[;1] like "*north*"} {m:.Q.a!x[1] rotate .Q.a; (x[1];m x[0])} each inp where {x[2]~5#key desc count each group asc x[0] except "-"} each inp
