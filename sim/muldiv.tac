; tac mul div reggression

       jmp start

.=     100
a=     mem 3
b=     mem 4
c=     mem 0

x=     mem 100
y=     mem 3
z=     mem 0

start: mul a b c
       div x y z
       hlt

; EOF
