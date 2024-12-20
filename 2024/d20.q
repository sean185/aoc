map:read0`:d20eg.txt
map:read0`:d20.txt
where2d:{raze (til count x),/:'where each x} // get 2d coords
d:(1 0;0 1;-1 0;0 -1)

// part 1 - slow!
track:{x,p where (not p in x)and(in[;".E"]map ./: p:d+\:last x)}/[where2d map="S"]
res:raze (til count track){2+x-y where y>x}'track ? (track+/:\:2*d) @/:' where each track{in[;("#.";"#E")]map ./: p:x+/:y*/:1 2}/:\:d
sum -100>=res

// part 1 alt, faster by pre-generating track IDs
visited:.[(2#count map)#0N;first where2d map="S";:;0]
track:() // just use globals, lazy
{track,:enlist x; if["E"=map . x;:x]; r:first np where (null visited ./: np)&(map ./: np:x+/:d)in".E"; visited::.[visited;r;:;1+visited . x]; r}/[first where2d map="S"]
sum raze -100>=0^(2+til count track)-{visited ./: x+/:d*2}each track

// part 2 - super slow, ~410s??
search:{x where 1<sum each abs x} 19{distinct raze d+\:/:x}/d,enlist 0 0
res:raze track{$[count[track]<=p:track ? x+y;0;(sum abs y)>=p-o:track ? x;0;(p-o)-(sum abs y)]}/:\:search
sum 100<=res

// part 2 alt, much faster now, ~1s
search:{x where 1<sum each abs x} 19{distinct raze d+\:/:x}/d,enlist 0 0
sum raze -100>=raze 0^(til count track)-(til count track){y where y>x}'{(neg sum flip abs search)+visited ./:x+/:search} each track
