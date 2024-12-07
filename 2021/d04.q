\cd C:\Repos\aoc2021\d04
txt:"\n\n" vs "\n" sv read0 `:d04eg.txt
txt:"\n\n" vs "\n" sv read0 `:d04.txt
seq:"J"$"," vs first txt
boards:value each ssr[;"  ";1#" "] each  ssr[;1#"\n";1#" "] each 1_txt
check:{any raze all each null {(x;flip x)}5 5#x}

// part1 - 10680
l:0N;
l*sum raze {[bs;i]
    if[any b:check each bs; :bs where b];
    l::i;
    {$[x in y; @[y;y?x;:;0N]; y]}'[i;bs]
 }/[boards;seq]

// part 1 - one liner ????????
check2:{any raze all each {(x;flip x)}5 5#x}
first @[;where r=min r] (seq r:sum each int)*sum each boards@'where each not int:{$[check2 x; x; x|y]}/'[boards =/:\: seq]


// part2 - 31892
i:0;
while[(i<count seq) and (1<count boards);
    boards:boards where not check each boards;
    boards:{$[x in y; @[y;y?x;:;0N]; y]}'[seq[i];boards];
    i+:1]
seq[i-1]*sum raze boards[0]

{[bs;i]
    if[0=count bs; :()];
    bs:{$[x in y; @[y;y?x;:;0N]; y]}'[i;bs];
    0N!r:i*sum each raze each bs where b:check each bs;
    if[0=count bs; l::r; :()];
    bs where not b
 }/[boards;seq]

// input : board, sequence
// output : board remainder, winning number