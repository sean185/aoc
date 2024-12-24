delete from `.
xor:{0b sv (<>). 0b vs'(x;y)}
txt:read0`:d24.txt
/ part 1
get each (txt ? "")#txt
get each {x[4],"::",(lower x[1]),"[",x[0],";",x[2],"]"} each " "vs' (1+txt ? "")_txt
2 sv get each desc {x where x like "z*"}key `.

/ part 2
/ do an addition where all x-bits are 0s, and all y-bits are 1s
/ then, manually step through to look for wires with output issues!
/ example of a CORRECT set of 5 gates
/ x?? XOR y?? -> aaa // intermediate step for position ?? 
/ x?? AND y?? -> bbb // check if carry is generated 
/ aaa XOR zzz -> z?? // combine residual carry into position ??
/ aaa AND zzz -> ccc // check if carry is generated (FINAL) 
/ bbb OR ccc -> ddd // add to carry line
get each {(-1_x),string $[x like "x*";0;1]} each (txt ? "")#txt
-1_1_ where differ get each asc {x where x like "z*"}key `.

// z06 z13 z25 z38
"," sv string asc `z06`jmq`z13`gmh`cbd`rqf`qrh`z38


\ 
// manually rewiring by identifying based on the pattern!

y00 XOR x00 -> z00 // 0th 
x00 AND y00 -> nqp // carry from 0th

x01 XOR y01 -> fht // 1st 
y01 AND x01 -> dmk // carry from 1st 
fht XOR nqp -> z01 // 1st position : intermediate + carry from 0th
nqp AND fht -> ntf // carry of 1st 
dmk OR ntf -> nrs // add to carry line

x02 XOR y02 -> qdt // 2nd
y02 AND x02 -> pbb // carry from 2nd
nrs XOR qdt -> z02 // apply carry to 2nd
nrs AND qdt -> mkc // carry of 2nd
pbb OR mkc -> bcm // add to carry line

x06 XOR y06 -> sfm
x06 AND y06 -> z06 // < should lead to a carry 
cjt XOR sfm -> jmq // < should be z06!
cjt AND sfm -> fmd
fmd OR jmq -> qsf

x13 XOR y13 -> nmm
x13 AND y13 -> fjv
nmm XOR kwb -> gmh // here!
nmm AND kwb -> gbd
gbd OR fjv -> z13 // ah ha


x25 XOR y25 -> cbd // wrong!
x25 AND y25 -> rqf // with this??
rqf XOR kdt -> z25
kdt AND rqf -> mrj
mrj OR cbd -> bjr


x38 XOR y38 -> njc
y38 AND x38 -> cpg
ngk XOR njc -> qrh // z wire should be here instead
njc AND ngk -> z38 // so swap!
cpg OR qrh -> wtp


