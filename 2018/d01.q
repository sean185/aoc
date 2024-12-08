inp:read0`:d01.txt
inp:", "vs"+1, -1"
inp:", "vs"+3, +3, +4, -2, -4"
inp:", "vs"-6, +3, +8, +5, -6"
inp:", "vs"+7, +7, -2, -7, -4"
// part 1
sum a:get except[;"+"]" "sv inp
// part 2, error out when reached
{r:(last x 1)+a x 0; if[r in x 1;'string r]; ((x[0]+1)mod count a;x[1],r)}/[(0;1#0)]
// extra attempt after doing python solution
({if[y in z;:(x;y;z)]; (x+1;y+a x mod count a;z,y)}.)/[(0;0;0#0)]