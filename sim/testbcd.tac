; shlc SHLA compilation Tue Aug  7 20:40:26 2018
; this assumes a TAC with 10 bit word width
; mem locs 1-255 are local local or temporary vars
RESET:	JMP MAIN
STKPTR:	MEM 255
FRMPTR:	MEM 255
.=	256
#PRAGMA	print a[10],b[10],c[10]
a=	MEM 0*10
b=	MEM 0*10
c=	MEM 0*10
d=	MEM 0
e=	MEM 0
x=	MEM 0
y=	MEM 0
u=	MEM 0
i=	MEM 0
DATA=	MEM 1
	MEM 2
	MEM 3
	MEM 4
	MEM 5
	MEM 1023
	MEM 0
	MEM 9
	MEM 8
	MEM 7
	MEM 6
	MEM 5
	MEM 1023
DATPTR=	MEM DATA
MAIN:	MOV #0 i
L00001:	MOV *DATPTR d
	ADD DATPTR #1 DATPTR
	ADD #a i 16
	MOV d *16
	CMP d #0
	JLE L00002
	ADD i #1 18
	MOV @18 i
	JMP L00001
L00002:	MOV #0 i
L00003:	MOV *DATPTR d
	ADD DATPTR #1 DATPTR
	ADD #b i 19
	MOV d *19
	CMP d #0
	JLE L00004
	ADD i #1 21
	MOV @21 i
	JMP L00003
L00004:	MOV #0 i
	MOV #0 u
	MOV #0 e
L00005:	ADD #a i 22
	MOV *22 x
	CMP x #0
	JEQ L00006
	JGT L00006
	MOV #0 x
	ADD e #1 24
	MOV @24 e
L00006:	ADD #b i 25
	MOV *25 y
	CMP y #0
	JEQ L00007
	JGT L00007
	MOV #0 y
	ADD e #1 27
	MOV @27 e
L00007:	CMP e #1
	JGT L00008
	ADD x y 30
	ADD @30 u 17
	MOV @17 d
	CMP d #9
	JEQ L00009
	JLE L00009
	MOV #1 u
	SUB d #10 19
	MOV @19 d
	JMP L00010
L00009:	MOV #0 u
L00010:	ADD #c i 20
	MOV d *20
	ADD i #1 22
	MOV @22 i
	JMP L00005
L00008:	CMP u #0
	JEQ L00011
	JLE L00011
	ADD #c i 23
	MOV u *23
	ADD i #1 25
	MOV @25 i
L00011:	ADD #c i 26
	COM #1 27
	MOV @27 *26
	HLT
HEAP:	MEM 0
