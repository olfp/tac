; shlc SHLA compilation Mon Mar  6 22:11:49 2017
; this assumes a TAC with 10 bit word width
; mem locs 10-99 are temp vars for expr eval
RESET:	JMP MAIN
.=	100
i=	MEM 0
a=	MEM 1014
b=	MEM 0
c=	MEM 0
n=	MEM 0*5
DATA=	MEM 42
	MEM 69
	MEM 96
	MEM 123
	MEM 2
	MEM 3
	MEM 4
	MEM 5
	MEM 1023
DATPTR=	MEM DATA
MAIN:	NOP
L00001:	MOV *DATPTR a
	ADD DATPTR #1 DATPTR
	MOV *DATPTR b
	ADD DATPTR #1 DATPTR
	CMP a #0
	JLE L00002
	ADD #n i 10
	MUL a b 11
	MOV 11 *10
	SUB i #1 12
	ADD #n 12 13
	MOV *13 c
	ADD i #1 14
	MOV 14 i
	JMP L00001
L00002:	HLT
