txt:"\n"vs'"\n\n" vs "\n" sv read0`:d25.txt
locks:{sum -1_1_"#"=x}each txt where all each "#"=first each txt
ks:{sum -1_1_"#"=x}each txt where all each "."=first each txt
sum raze locks{all 5>=x+y}\:/:ks