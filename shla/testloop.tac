; TACcc compilation Fri Mar  3 17:26:40 2017
; mem locs 1-99 are temp vars for expr eval
RESET:	JMP MAIN
.=	100
a=	MEM 42
b=	MEM 69
c=	MEM 96
i=	MEM 0
MAIN:	MOV #69 i
	CMP i #42
	JEQ L00001
	JLE L00001
	MUL #2 a 0
	ADD 0 b 1
	MUL 1 c 2
	SUB 2 #3 3
	MOV 3 i
L00001:	MOV #0 i
L00002:	ADD i #1 4
	MOV 4 i
	CMP i #3
	JEQ L00003
	JMP L00002
L00003:	HLT
