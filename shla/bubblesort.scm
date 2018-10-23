; bubblesort in scheme
; https://repl.it/repls/UsedZanySyndrome

(define (bubble-sort x)
  (letrec
    ((fix (lambda (f i)
       (if (equal? i (f i))
           i
           (fix f (f i)))))

     (sort-step (lambda (l)
        (if (or (null? l) (null? (cdr l)))
            l
            (if (> (car l) (cadr l))
                (cons (cadr l) (sort-step (cons (car l) (cddr l))))
                (cons (car  l) (sort-step (cdr l))))))))

  (fix sort-step x)))

(bubble-sort (list 43 96 69 13 21 7 66 69 99 1))
