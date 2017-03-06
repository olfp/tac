;
; 0-th tac test
;

	jmp start

.=	100			; init mem ptr
a=	mem 1			; init loc 100 to 1
b=	mem 7			; init loc 101 to 7
i=	mem 0
n=	mem 3
c=	mem 15
d=	mem 0
z=	mem i
q=	mem 0

start:	mov #6 100		; 6 -> loc 100
       	mov #7 b		; 7 -> loc b (101)
loop:  	add 100 b i		; loc 100 + loc 101 -> loc 102
	sub i c d
	mov #42 *z
	com *z q
	not q q
	shl q q
	add #666 #555 q
	nop
	nop
	ror #3 q
	clc

	mov #10 i
	com i i
for:	nop
	add i #1 i
	; cmp n i
	jlz for

       	hlt

; EOF
