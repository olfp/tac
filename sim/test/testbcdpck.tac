; shlc SHLA compilation Tue Aug  7 20:32:07 2018
; this assumes a TAC with 10 bit word width
; mem locs 1-255 are local local or temporary vars
RESET:	JMP MAIN
STKPTR:	MEM 255
FRMPTR:	MEM 255
.=	256
#PRAGMA	bits 12
#PRAGMA	read bcd.dat@heap
#PRAGMA	print z1[10],z2[10],res[10]
z1=	MEM 0*10
z2=	MEM 0*10
res=	MEM 0*10
digpergrp=	MEM 3
putbcd:	MEM 0
	ADD FRMPTR #1 16
	MOV putbcd *16
L00001:	SUB FRMPTR #3 16
	CMP *16 #1
	JLE L00002
	SUB FRMPTR #0 16
	SHL *16 16
	SHL 16 16
	SHL 16 16
	SHL 16 16
	SUB FRMPTR #0 17
	MOV @16 *17
	SUB FRMPTR #3 17
	SUB *17 #1 18
	SUB FRMPTR #3 19
	MOV @18 *19
	JMP L00001
L00002:	SUB FRMPTR #1 19
	MOV *19 19
	SUB FRMPTR #2 19
	ADD @19 *19 19
	SUB FRMPTR #1 20
	MOV *20 20
	SUB FRMPTR #2 20
	ADD @20 *20 20
	SUB FRMPTR #0 22
	IOR *20 *22 23
	MOV @23 *19
	MOV FRMPTR STKPTR
	ADD STKPTR #1 STKPTR
	MOV *STKPTR 24
	ADD STKPTR #1 STKPTR
	MOV *STKPTR FRMPTR
	JMP *24
getbcd:	MEM 0
	ADD FRMPTR #1 24
	MOV getbcd *24
	SUB FRMPTR #1 24
	MOV *24 24
	SUB FRMPTR #2 24
	ADD @24 *24 24
	SUB FRMPTR #0 25
	MOV *25 25
	MOV *24 *25
L00003:	SUB FRMPTR #3 25
	CMP *25 #1
	JLE L00004
	SUB FRMPTR #0 25
	MOV *25 25
	SHR *25 25
	SHR 25 25
	SHR 25 25
	SHR 25 25
	SUB FRMPTR #0 26
	MOV *26 26
	MOV @25 *26
	SUB FRMPTR #3 26
	SUB *26 #1 27
	SUB FRMPTR #3 28
	MOV @27 *28
	JMP L00003
L00004:	SUB FRMPTR #0 28
	MOV *28 28
	AND *28 #15 29
	SUB FRMPTR #0 30
	MOV *30 30
	MOV @29 *30
	MOV FRMPTR STKPTR
	ADD STKPTR #1 STKPTR
	MOV *STKPTR 30
	ADD STKPTR #1 STKPTR
	MOV *STKPTR FRMPTR
	JMP *30
readbcd2p:	MEM 0
	ADD FRMPTR #1 30
	MOV readbcd2p *30
	SUB FRMPTR #2 30
	MOV #0 *30
	SUB FRMPTR #3 30
	MOV #1 *30
	SUB FRMPTR #4 30
	MOV #1 *30
L00005:	SUB FRMPTR #1 30
	MOV *DATPTR *30
	ADD DATPTR #1 DATPTR
	SUB FRMPTR #1 30
	CMP *30 #9
	JGT L00006
	SUB FRMPTR #1 30
	AND *30 #15 31
	MOV FRMPTR 16
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	MOV @31 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 16 #0 17
	MOV *17 17
	MOV 17 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 16 #4 17
	MOV 17 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 16 #2 17
	MOV 17 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR putbcd
	SUB FRMPTR #3 17
	ADD *17 #1 18
	SUB FRMPTR #3 19
	MOV @18 *19
	SUB FRMPTR #2 19
	ADD *19 #1 20
	SUB FRMPTR #2 21
	MOV @20 *21
	SUB FRMPTR #2 21
	CMP *21 digpergrp
	JLE L00007
	SUB FRMPTR #2 21
	MOV #0 *21
	SUB FRMPTR #4 21
	ADD *21 #1 22
	SUB FRMPTR #4 23
	MOV @22 *23
L00007:	JMP L00005
L00006:	SUB FRMPTR #0 23
	MOV *23 23
	ADD @23 #0 23
	SUB FRMPTR #3 24
	SUB *24 #1 25
	MOV @25 *23
	MOV FRMPTR STKPTR
	ADD STKPTR #1 STKPTR
	MOV *STKPTR 26
	ADD STKPTR #1 STKPTR
	MOV *STKPTR FRMPTR
	JMP *26
sumbcd:	MEM 0
	ADD FRMPTR #1 26
	MOV sumbcd *26
	SUB FRMPTR #3 26
	MOV #0 *26
	SUB FRMPTR #4 26
	MOV #1 *26
	SUB FRMPTR #5 26
	MOV #1 *26
	SUB FRMPTR #6 26
	MOV #0 *26
L00008:	SUB FRMPTR #7 26
	MOV #0 *26
	SUB FRMPTR #0 26
	MOV *26 26
	ADD @26 #0 26
	SUB FRMPTR #4 27
	CMP *26 *27
	JEQ L00009
	JGT L00009
	SUB FRMPTR #8 27
	MOV #0 *27
	SUB FRMPTR #7 27
	ADD *27 #1 28
	SUB FRMPTR #7 29
	MOV @28 *29
	JMP L00010
L00009:	MOV FRMPTR 29
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	SUB 29 #8 30
	MOV 30 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 29 #0 30
	MOV *30 30
	MOV 30 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 29 #5 30
	MOV 30 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 29 #6 30
	MOV 30 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR getbcd
L00010:	SUB FRMPTR #1 30
	MOV *30 30
	ADD @30 #0 30
	SUB FRMPTR #4 31
	CMP *30 *31
	JEQ L00011
	JGT L00011
	SUB FRMPTR #9 31
	MOV #0 *31
	SUB FRMPTR #7 31
	ADD *31 #1 16
	SUB FRMPTR #7 17
	MOV @16 *17
	JMP L00012
L00011:	MOV FRMPTR 17
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	SUB 17 #9 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 17 #1 18
	MOV *18 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 17 #5 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 17 #6 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR getbcd
L00012:	SUB FRMPTR #7 18
	CMP *18 #1
	JGT L00013
	SUB FRMPTR #8 18
	SUB FRMPTR #9 19
	ADD *18 *19 20
	SUB FRMPTR #3 22
	ADD @20 *22 23
	SUB FRMPTR #10 24
	MOV @23 *24
	SUB FRMPTR #10 24
	CMP *24 #9
	JEQ L00014
	JLE L00014
	SUB FRMPTR #3 24
	MOV #1 *24
	SUB FRMPTR #10 24
	SUB *24 #10 25
	SUB FRMPTR #10 26
	MOV @25 *26
	JMP L00015
L00014:	SUB FRMPTR #3 26
	MOV #0 *26
L00015:	MOV FRMPTR 26
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	SUB 26 #10 27
	MOV 27 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 26 #2 27
	MOV *27 27
	MOV 27 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 26 #5 27
	MOV 27 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 26 #6 27
	MOV 27 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR putbcd
	SUB FRMPTR #6 27
	ADD *27 #1 28
	SUB FRMPTR #6 29
	MOV @28 *29
	SUB FRMPTR #6 29
	CMP *29 digpergrp
	JLE L00016
	SUB FRMPTR #6 29
	MOV #0 *29
	SUB FRMPTR #5 29
	ADD *29 #1 30
	SUB FRMPTR #5 31
	MOV @30 *31
L00016:	SUB FRMPTR #4 31
	ADD *31 #1 16
	SUB FRMPTR #4 17
	MOV @16 *17
	JMP L00008
L00013:	SUB FRMPTR #3 17
	CMP *17 #0
	JEQ L00017
	JLE L00017
	MOV FRMPTR 17
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	SUB 17 #3 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 17 #2 18
	MOV *18 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 17 #5 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	SUB 17 #6 18
	MOV 18 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR putbcd
	SUB FRMPTR #4 18
	ADD *18 #1 19
	SUB FRMPTR #4 20
	MOV @19 *20
L00017:	SUB FRMPTR #2 20
	MOV *20 20
	ADD @20 #0 20
	SUB FRMPTR #4 21
	SUB *21 #1 22
	MOV @22 *20
	MOV FRMPTR STKPTR
	ADD STKPTR #1 STKPTR
	MOV *STKPTR 23
	ADD STKPTR #1 STKPTR
	MOV *STKPTR FRMPTR
	JMP *23
MAIN:	MOV FRMPTR 23
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	MOV #z1 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR readbcd2p
	MOV FRMPTR 24
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	MOV #z2 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR readbcd2p
	MOV FRMPTR 25
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	MOV #z1 *STKPTR
	SUB STKPTR #1 STKPTR
	MOV #z2 *STKPTR
	SUB STKPTR #1 STKPTR
	MOV #res *STKPTR
	SUB STKPTR #1 STKPTR
	JSR sumbcd
	HLT
HEAP:	MEM 0
