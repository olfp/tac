; shlc SHLA compilation Mon Mar  6 14:26:09 2017
; mem locs 10-99 are temp vars for expr eval
RESET:	JMP MAIN
.=	100
i=	MEM 0
n=	MEM 0
j=	MEM 0
l=	MEM 0
k=	MEM 42
m=	MEM 7
odd:  	MEM 0
	MOV #1 i
	JMP *odd
even: 	MEM 0
	MOV #0 i
	JMP *even
MAIN:	NOP
L00001:	CMP i #0
	JNE L00002
	JSR odd
	JMP L00003
L00002:	JSR even
L00003:	ADD j #1 10
	MOV 10 j
	CMP j #9
	JGT L00004
	JMP L00001
L00004:	HLT
