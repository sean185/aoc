t:"S: "0:/: "  " vs " " sv read0 `:day4.txt
t:"S: "0:/: read0 `:day4a.txt
// part 1
sum {all `byr`iyr`eyr`hgt`hcl`ecl`pid in x} each t[;0]
// part 2
p:(uj/){enlist x!y}.'t
p:select from p where (1920<="J"$byr), (2002>="J"$byr)
p:select from p where (2010<="J"$iyr), (2020>="J"$iyr)
p:select from p where (2020<="J"$eyr), (2030>="J"$eyr)
p:select from p where any each (`$ecl) in\: `amb`blu`brn`gry`grn`hzl`oth
p:select from p where 9=count each pid, all each (pid) in\: .Q.n
p:select from p where "#"=first each hcl, all each (1_'hcl) in\: "0123456789abcdef"
p:update hgt:"J"$-2_'hgt, ht:-2#'hgt from p
p:(select from p where ht like "in", hgt>=59, hgt<=76),(select from p where ht like "cm", hgt>=150, hgt<=193)
count p
