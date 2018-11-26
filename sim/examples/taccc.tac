; TACcc compilation Wed Mar  1 16:10:49 2017
; mem locs 0-99 are temp vars for expr eval
.=	100
a=	MEM 0
b=	MEM 10
MAIN:	NOP
L00001:	CMP a b
	JLZ L00002
	JZE L00002
	ADD a #1 0
	MOV 0 a
	JMP L00001
L00002:	HLT
