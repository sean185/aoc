a:"J"$csv vs "2,1,10,11,0,6"
a:0 3 6
target:2020; l:last a; j:-1+count a; pos:(-1 _ a)!(til j)
// 3 11344

target:300000; l:last a; j:-1+count a; pos:(-1 _ a)!(til j)
// 3745 1311824

target:3000000; l:last a; j:-1+count a; pos:(-1 _ a)!(til j)
// 278906 10486864

target:30000000; l:last a; j:-1+count a; pos:(-1 _ a)!(til j)
\ts while[target>j;
    n:pos[l];
    pos[l]:j;
    l:0^j-n;
    j+:1;
    ]

where pos=max pos