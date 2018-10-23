( bubblesort demo in forth )
( https://www.tutorialspoint.com/execute_forth_online.php )

: bubble ( addr cnt -- )
  dup 1 do
    2dup i - cells bounds do
      i 2@ < if i 2@ swap i 2! then
    cell +loop
  loop ;

: aprint ( addr cnt -- )
  cells bounds do
    i @ .
  cell +loop ;

create data 43 , 96 , 69 , 13 , 21 , 7 , 66 , 69 , 99 , 1 ,
data 10 bubble
data 10 aprint
