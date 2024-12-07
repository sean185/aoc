inp:"abc"
inp:"reyedfim"
// part 1
f:{h:md5 x,string y; $[(0x0000~2#h)and(0x10>h[2]);y;y+1]}[inp;]/
d:1_ 8 {f x+1}\ 0
{@[;5]""sv string md5 inp,string x}each d
// part 2
f:{h:md5 x,string y; $[(0x0000~2#h)and(0x08>h[2]);y;y+1]}[inp;]/
d:1_ 16 {f x+1}\ 0
{m:x[;6](first each group x[;5]); raze m string til 8}{""sv string md5 inp,string x} each d
