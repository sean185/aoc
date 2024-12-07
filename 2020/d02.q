l:read0`:day2.txt
t:{`minc`maxc`ch`str!("J"$"-" vs x[0]),(-1_x[1]),2_ x} each " " vs/:l
// part 1
count {select from x where c>=minc, c<= maxc} update c:sum each str='ch from t
// part 2
{select from x where hasc1<>hasc2} select hasc1:ch=str@'minc-1, hasc2:ch=str@'maxc-1 from t
