; shlc SHLA compilation Tue Aug  7 22:14:29 2018
; this assumes a TAC with 10 bit word width
; mem locs 1-255 are local local or temporary vars
RESET:	JMP MAIN
STKPTR:	MEM 255
FRMPTR:	MEM 255
.=	256
#PRAGMA	print ctab[10],stab[10],mtab[10]
cnt=	MEM 0
sum=	MEM 0
pro=	MEM 1
ctab=	MEM 0*10
stab=	MEM 0*10
mtab=	MEM 0*10
MAIN:	MOV #0 cnt
L00001:	ADD cnt #1 17
	MOV @17 cnt
	SUB cnt #1 19
	ADD #ctab @19 20
	MOV cnt *20
	CMP cnt #9
	JGT L00002
	JMP L00001
L00002:	MOV #0 cnt
L00003:	ADD cnt #1 22
	MOV @22 cnt
	ADD sum cnt 25
	MOV @25 sum
	SUB cnt #1 27
	ADD #stab @27 28
	MOV sum *28
	CMP cnt #9
	JGT L00004
	JMP L00003
L00004:	MOV #0 cnt
L00005:	ADD cnt #1 30
	MOV @30 cnt
	MUL pro cnt 17
	MOV @17 pro
	SUB cnt #1 19
	ADD #mtab @19 20
	MOV pro *20
	CMP cnt #9
	JGT L00006
	JMP L00005
L00006:	HLT
HEAP:	MEM 0
