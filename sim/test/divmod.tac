; divmod

start:	div a b res
	hlt

a:	mem 42
b:	mem 10
res: 	mem 0
mod:	mem 0

#pragma print res,mod

; eof
