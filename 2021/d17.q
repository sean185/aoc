\cd C:\Repos\aoc2021\d17
eg:"target area: x=20..30, y=-10..-5"
qn:"target area: x=124..174, y=-123..-86"
simx:{[x;n] n {0 or x-1}\ x}
simy:{[y;n] n {x-1}\ y}
// part 1 = 7503
/
max
dy/dt -> vy - t = 0
max vy < max delta y
-122
\
{(simx[x;z-1];simy[y;z-1])}[6;10;20]
sums each {(simx[x;z-1];simy[y;z-1])}[6;10;22]
max each sums each {(simx[x;z-1];simy[y;z-1])}[30;122;246]
// part 2 - 3229
/
vy_min = y_grid
vy_max = abs(y_grid-1)
work backwards to get t
within time t, x must reach y_grid
vx_max = 30
vx_min = 
get vx
\
sum til 17
/eg
dx:20 30
dy:-10 -5
vx:6 30
vy:-10 9
/d17
dx:124 174
dy:-123 -86
vx:10 174
vy:-123 122

range:{x + til 1+y-x}
check:{[x;y;z] any {(x within dx) and (y within dy)} ./: flip (sums simx[x;z-1];sums simy[y;z-1])}
count l where check[;;30] ./: l:(range . vx) cross (range . vy)
count l where check[;;246] ./: l:(range . vx) cross (range . vy)
