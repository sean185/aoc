// part 1
t:([]c:cross/[6 10#til 10]);
t:select from t where {all 0<= deltas x} each c;
t:select from t where ("J"$raze each string c) within (134564 585159);
t:select from t where (count each c)>(count each distinct each c);
count[t]; // 1929

// part 2
t:select from t where {2 in value count each group x} each c;
count[t]; // 1306
