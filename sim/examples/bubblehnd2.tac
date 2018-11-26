; bubblesort in handcrafted tac
; basic version sort 10 values

init:   jmp start

; data field 43 96 69 13 21 7 66 69 99 1
data:   mem 43
        mem 96
        mem 69
        mem 13
        mem 21
        mem 7
        mem 66
        mem 69
        mem 99
        mem 1

t:      mem 0                           ; temp var for swap
i:      mem 0                           ; inner loop counter
n:      mem 0                           ; index of swapped item
o:      mem 9                           ; inner loop upper bound

start:  mov #1 n                        ; reset upper bound to min
        mov #0 i                        ; reset lower bound
loop:   beq i o break                   ; upper bound reached?
        ble *i(data) *i(data+1) skip    ; data[i] <= data[i+1]?
        mov *i(data) t                  ; swap, data[i] > data[i+1]
        mov *i(data+1) *i(data)
        mov t *i(data+1)
        add i #1 n                      ; remember index
skip:   add i #1 i                      ; next iteration
        jmp loop
break:  mov n o                         ; last swap is new upper bound
        bgt o #1 start                  ; stop if less the two unsorted
        hlt

#pragma print data[10]

; eof
