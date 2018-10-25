MODULE BubbleSort3;

    IMPORT Out, Strings, StringScan;

    CONST TestNums = "43 96 69 13 21 7 66 69 99 1";

    TYPE Elem = POINTER TO RECORD
                    v: INTEGER;
                    next: Elem;
                END;

    VAR n, i, o, on: INTEGER; data, this, next: Elem;

    PROCEDURE Swap(VAR a: INTEGER; VAR b: INTEGER);
        VAR t: INTEGER;
    BEGIN
        t := a;
        a := b;
        b := t;
    END Swap;

    PROCEDURE Parse(str: ARRAY OF CHAR; VAR c: INTEGER): Elem;
        VAR i, n: INTEGER;
            h, p, q: Elem;
    BEGIN
        i := 0;
        c := 0;
        q := NIL; (* last Elem *)
        WHILE(i < Strings.Length(TestNums)) DO
    	    StringScan.StrToIntPos(TestNums, n, i);
            INC(c);
            NEW(p);
            p.v := n;
            p.next := NIL;
            IF q # NIL THEN
                q.next := p;
            ELSE (* first elem *)
                h := p;
            END;
            q := p;
        END;
        RETURN h;
    END Parse;

    PROCEDURE OutList(data: Elem);
    BEGIN
        WHILE data # NIL DO
            Out.Int(data.v, 0);
            IF data.next # NIL THEN
                Out.String(", ");
            END;
            data := data.next;
        END;
        Out.Ln;
    END OutList;

BEGIN
    data := Parse(TestNums, n);
    (* now sort *)
    o := n - 1;
    WHILE( o > 1) DO
        on := 1;
        this := data;
        next := this.next;
        FOR i := 0 TO o - 1 DO
            IF this.v > next.v THEN
                Swap(this.v, next.v);
                on := i+1;
            END;
            this := next;
            next := this.next;
        END;
        o := on;
    END;
    (* print sorted array *)
    OutList(data);
END BubbleSort3.
