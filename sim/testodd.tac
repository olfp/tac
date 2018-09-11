; shlc SHLA compilation Tue Mar  7 21:16:54 2017
; this assumes a TAC with 10 bit word width
; mem locs 10-99 are temp vars for expr eval
RESET:	JMP MAIN
.=	100
n=	MEM 0
res=	MEM 0*10
i=	MEM 0
DATA=	MEM 1
	MEM 2
	MEM 3
	MEM 4
	MEM 5
	MEM 6
	MEM 7
	MEM 1023
DATPTR=	MEM DATA
MAIN:	MOV #0 i
L00001:	MOV *DATPTR n
	ADD DATPTR #1 DATPTR
	CMP n #0
	JLE L00002
	DIV n #2 10
	MUL 10 #2 11
	CMP n 11
	JEQ L00003
	ADD #res i 12
	MOV n *12
	ADD i #1 13
	MOV 13 i
L00003:	JMP L00001
L00002:	HLT
