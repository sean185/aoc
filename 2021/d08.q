\cd C:\Repos\aoc2021\d08
digits:("abcefg";"cf";"acdeg";"acdfg";"bcdf";"abdfg";"abdefg";"acf";"abcdefg";"abcdfg")

t:" " vs "cdfeb fcadb cdfeb cdbaf"
t like/: digits
(count each digits)[1 4 7 8]
group count each digits
sum raze {x in 2 4 3 7} each (count'') " " vs/: last each " | " vs/:  read0 `:d08.txt
read0 `:d08eg.txt
// part 2

{(2 4 3 7!1 4 7 8)x} each (count'') " " vs/: 
findmapping:{
    t:" " vs x;
    c:count each t;
    m:10#0N;
    m[1 4 7 8]:c?2 4 3 7;
    m[3]:first i2or3or5 where all each t[m[1]] in/:fives:t[i2or3or5:where c=5];
    i2or5:i2or3or5 except m[3];
    m2or5:(5 2)3=count each t[i2or5] except\: t[m[4]];
    m[m2or5]:i2or5;
    m[9]:first i0or6or9 where all each t[m[4]] in/: sixes:t[i0or6or9:where c=6];
    i0or6:i0or6or9 except m[9];
    m0or6:(6 0) all each t[m[1]] in/: t[i0or6];
    m[m0or6]:i0or6;
    m
 } 
crunch:{m:(`$asc each " "vs x[0]) findmapping x[0];m ? `$asc each " " vs x[1]}
sum 10 sv/: crunch each " | " vs/:  read0 `:d08.txt

map:(1110111b;0010010b;1011101b;1011011b;1110100b;1101011b;1101111b;1010010b;1111111b)



{
    t:" " vs x;
    m:1 4 7 8!t(count each t)? 2 4 3 7;
    d:""!"";
    d[m[7] except m[1]]:"a";
    d
    }
    first first " | " vs/:  read0 `:d08eg.txt
\
1 4 7 8
a:7-1
e:8-0
c:8-6
d:8-0
f:1-c
b:4-1-d
g:9-4-a


2 = count --> 1   2
3 = count --> 7   2+1
4 = count --> 4   2  +2
7 = count --> 8   2+1+2+2

              2   
              3
              5
              6  
   ???????
   abcdefg
0: xxx xxx
1:   x  x 
2: x xxx x
3: x xx xx
4: xxx  x 
5: xx x xx
6: xx xxxx
7: x x  x 
8: xxxxxxx
9: xxxx xx