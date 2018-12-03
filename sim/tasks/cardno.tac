; check card number
; 1. card number is in mem in four mem cells, seperate digits
; A word must hold a four digit decimal, so min. 14 bits are needed

#pragma bits 14
#pragma print cardno[4]

init:   jmp start

start:  nop


finish: hlt

cardno: mem 0*4

; eof
