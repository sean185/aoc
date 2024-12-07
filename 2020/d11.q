t:read0`:day11eg.txt
t:read0`:day11.txt
findadj:{[t;p] t ./: p+/:(-1 -1; -1 0; -1 1; 0 1; 1 1; 1 0; 1 -1; 0 -1)}
/ findadj[t;1 1]
// part 1
sum "#"=raze res:{[t]
    w:count t;
    l:count first t;
    (w;l)# {[t;p] s:t . p; adj:findadj[t;p];
        if[(s="L") and 0=sum "#"=adj; :"#"];
        if[(s="#") and 4<=sum "#"=adj; :"L"];
        s
        }[t;] each (til w) cross til l
    }/[t]

// part 2
findadj2:{[t;p;w;l] m:1+til (min w,l)-1; {first x where x in "#L"} each t ./:/: flip each p+/:(m;m)*/: (-1 -1; -1 0; -1 1; 0 1; 1 1; 1 0; 1 -1; 0 -1)}
findadj2[t;0 9;w;l]
\ts sum "#"=raze res:{[t]
    w:count t;
    l:count first t;
    r:(w;l)#{[t;p;w;l]
        s:t . p;
        adj:findadj2[t;p;w;l];
        if[(s="L") and 0=sum "#"=adj; :"#"];
        if[(s="#") and 5<=sum "#"=adj; :"L"];
        s
        }[t;;w;l] each (til w) cross til l
    }/[t]
// 217085 778368

