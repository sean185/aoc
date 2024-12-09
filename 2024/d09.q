inp:raze read0`:d09eg.txt
inp:raze read0`:d09.txt
inp:"12345"
make:{a:0N 2#"J"$'x,"0"; n:{x#'til count x}first each a; raze n,'((last each a)#\:0N)}
f:{if[null p:first where null x; :x]; if[not null n:last x; x[p]:n]; -1_x}/
check:{sum(til count x)*x}
check f make inp
6323641412437

// for each iteration
// - identify target block based on counter
// - identify available spaces
// - find the first that has the matching size
// - slot in, and return
f:{[x;i]
    c:count p:where x=i;
    spaces:value a group sums not 1=deltas a:where null x;
    if[all c>count each spaces; :x]; // move only if there is space
    np:first spaces where c<=count each spaces;
    if[first[np]>last p; :x]; // move only if it moves left
    @[x;p,c#np;:;(c#0N),x p]
    }
check {x f/reverse til 1+last x} make inp
6351801932670
