txt:read0`:d15eg.txt
txt:read0`:d15.txt
map:(txt?"")#txt
d:"^v<>"!(-1 0;1 0;0 -1;0 1); moves:d raze(1+txt?"")_txt
where2d:{raze (til count x),/:'where each x} // get 2d coords
// find a space that is in the direction of move, or return null if encountered no spaces at all
// determine "@"
// recursively find all the next tile in the direction of travel until a space is found, or otherwise
rc:{[map;curr;dir] if["."=map . curr; :curr]; nxt:curr + dir; $["#"=map . nxt; curr; nxt]}
f:{[mp;mv] r:first where2d "@"=mp; nt:mp ./: np:rc[mp;;mv]\[r]; if[(1=n:count np)or(not "."in nt);:mp]; .[;;:;]/[mp;np;-1 rotate nt]}
chk:{sum raze 100 1*/:where2d "O"=x}
chk {-1 x;x}map f/moves
// part 2
// but now, curr is a list of points! like a wavefront...
map:ssr[;"@";"@."]each ssr[;".";".."]each ssr[;"O";"[]"]each ssr[;"#";"##"]each map
rc:{[map;curr;dir] if[any"#"=t:map ./: curr;:curr]; nt:map ./: nxt:curr +\: dir; r where not "."=map ./:r:distinct nxt,$[0=dir 1;{x+0,0^("[]"!1 -1)y}'[nxt;nt];()]}
chk:{sum raze 100 1*/:where2d "["=x}
f:{[mp;mv] r:where2d "@"=mp; np:rc[mp;;mv]\[r]; if[(1=n:count np)or("#"in (raze/) nt:mp ./:/: np);:mp]; mp:.[;;:;"."]/[mp;raze np]; .[;;:;]/[mp;mv+/:raze np;raze nt]}
chk {-1 x;x}map f/moves
