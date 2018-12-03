; check card number
; 1. card number is in mem in four mem cells, seperate digits, reverse
; A word must hold a four digit decimal, so min. 14 bits are needed
; 2. double every second digit. if > 9, subtract 9
; 3. sum all digits, last digit of sum must be zero

#pragma bits 14
#pragma print cardno[4]
#pragma print chknul[1]

init:   jmp start

grpidx:	mem 3

digidx:	mem 0
digcnt:	mem 0

tgrp:	mem 0
tmod:	mem 0

start:  mov cardno(grpidx) tgrp
	mov #0 digcnt
grplop:	div tgrp #10 tgrp
	mov tmod digits(digidx)
	add digidx #1 digidx
	add digcnt #1 digcnt
	bne digcnt #4 grplop
	sub grpidx #1 grpidx
	bge grpidx #0 start
	; now digits holds number in reverse order
	mov #1 digidx
double:	shl digits(digidx) digits(digidx)
	ble digits(digidx) #9 nodbl
	sub digits(digidx) #9 digits(digidx)
nodbl:	add digidx #2 digidx
	blt digidx #16 double
	; now sum up all digits
	mov #0 digidx
sumlop:	add chksum digits(digidx) chksum
	add digidx #1 digidx
	blt digidx #16 sumlop
	div chksum #10 chksum
finish: hlt

cardno: mem 0*4
digits:	mem 0*16
chksum:	mem 0
chknul: mem 42

; eof
