; shlc SHLA compilation Wed Sep 12 16:09:01 2018
; this assumes a TAC with 10 bit word width
; mem locs 1-255 are local local or temporary vars
RESET:	JMP MAIN
STKPTR:	MEM 255
FRMPTR:	MEM 255
.=	256
#PRAGMA	print a,b
a:	MEM 2
b:	MEM 3
plusone:	MEM 0
	ADD FRMPTR #1 16
	MOV plusone *16
	SUB FRMPTR #0 16
	MOV *16 16
	SUB FRMPTR #1 17
	ADD *16 *17 18
	SUB FRMPTR #0 19
	MOV *19 19
	MOV 18 *19
	MOV FRMPTR STKPTR
	ADD STKPTR #1 STKPTR
	MOV *STKPTR 19
	ADD STKPTR #1 STKPTR
	MOV *STKPTR FRMPTR
	JMP *19
plustwo:	MEM 0
	ADD FRMPTR #1 19
	MOV plustwo *19
	SUB FRMPTR #0 19
	MOV *19 19
	SUB FRMPTR #1 20
	ADD *19 *20 21
	SUB FRMPTR #0 22
	MOV *22 22
	MOV 21 *22
	MUL a #2 23
	SUB FRMPTR #1 24
	MOV 23 *24
	MOV FRMPTR 24
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	SUB 24 #0 25
	MOV *25 25
	MOV 25 *STKPTR
	SUB STKPTR #1 STKPTR
	MOV #42 *STKPTR
	SUB STKPTR #1 STKPTR
	JSR plusone
	MOV FRMPTR STKPTR
	ADD STKPTR #1 STKPTR
	MOV *STKPTR 25
	ADD STKPTR #1 STKPTR
	MOV *STKPTR FRMPTR
	JMP *25
MAIN:	MOV FRMPTR 25
	MOV FRMPTR *STKPTR
	SUB STKPTR #2 STKPTR
	MOV STKPTR FRMPTR
	MOV #a *STKPTR
	SUB STKPTR #1 STKPTR
	MOV b *STKPTR
	SUB STKPTR #1 STKPTR
	JSR plustwo
	HLT
HEAP:	MEM 0