MODULE BubbleSort2;

    IMPORT Out, Strings, StringScan;

    CONST TestNums = "43 96 69 13 21 7 66 69 99 1";

    TYPE PIA = POINTER TO ARRAY OF INTEGER;

    VAR n, i, o, on: INTEGER; data: PIA;

    PROCEDURE Swap(VAR a: INTEGER; VAR b: INTEGER);
        VAR t: INTEGER;
    BEGIN
        t := a;
        a := b;
        b := t;
    END Swap;

    PROCEDURE WordCount(CONST str: ARRAY OF CHAR): INTEGER;
        VAR i, n: INTEGER;
    BEGIN
        i := 0; n := 1;
        WHILE str[i] # 0X DO
            IF str[i] = " " THEN
                INC(n);
            END;
            INC(i);
        END;
        RETURN n;
    END WordCount;

    PROCEDURE Parse(str: ARRAY OF CHAR): PIA;
        VAR i, j, w: INTEGER;
            p: PIA;
    BEGIN
        w := WordCount(str);
        NEW(p, w);
        i := 0;
        j := 0;
        WHILE(i < Strings.Length(TestNums)) DO
    	   StringScan.StrToIntPos(TestNums, p[j], i);
           INC(j);
        END;
        RETURN p;
    END Parse;

BEGIN
    data := Parse(TestNums);
    (* now sort *)
    n := LEN(data^) - 1;
    o := n;
    WHILE( o > 1) DO
        on := 1;
        FOR i := 0 TO o - 1 DO
            IF data[i] > data[i+1] THEN
                Swap(data[i], data[i+1]);
                on := i+1;
            END;
        END;
        o := on;
    END;
    (* print sorted array *)
    FOR i := 0 TO n DO
        Out.Int(data[i], 0);
        Out.String(", ");
    END;
    Out.Ln;
END BubbleSort2.
