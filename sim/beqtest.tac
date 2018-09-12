; test beq

start: mov #12 a
       beq a b label
       add #42 a a
       jmp end
label: mov a b
end:   hlt

; vars

a:     mem 0
b:     mem 42
c:     mem 69
