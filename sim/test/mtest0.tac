; manual base function test for tacsim
; set bitsize large enough (20) or observe overflow in test 3

run:	jmp count

; define vars

cnt=	mem 42
tptr=   mem 69
ctab=	mem 0*10
sum=	mem 0
stab=	mem 0*10
pro=    mem 1
mtab=   mem 0*10

; 1. count to ten

#pragma print ctab[10]

count:	mov #0 cnt
loop:	add #ctab cnt tptr
	add cnt #1 cnt
	mov cnt *tptr
	cmp cnt #10
	jle loop

; 2. count to ten while summing up

#pragma print stab[10]

sumup:	mov #0 cnt
suml:	add #stab cnt tptr
	add cnt #1 cnt
	add sum cnt sum
	mov sum *tptr
	cmp cnt #10
	jle suml

; 3. count to ten while multiplying

#pragma print mtab[10]

mulup:  mov #0 cnt
mull:   add #mtab cnt tptr
        add cnt #1 cnt
        mul pro cnt pro
        mov pro *tptr
        cmp cnt #10
        jle mull
	
finish:	hlt


; EOF
