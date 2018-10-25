MODULE BubbleSort;

    IMPORT Out, Strings, StringScan;

    CONST TestNums = "43 96 69 13 21 7 66 69 99 1";

    VAR i, o, on: INTEGER; data: ARRAY 10 OF INTEGER;

    PROCEDURE Swap(VAR a: INTEGER; VAR b: INTEGER);
        VAR t: INTEGER;
    BEGIN
        t := a;
        a := b;
        b := t;
    END Swap;

    PROCEDURE Fill(VAR arr: ARRAY OF INTEGER);
        VAR i, j: INTEGER;
    BEGIN
        i := 0;
        j := 0;
        WHILE(i < Strings.Length(TestNums)) DO
    	   StringScan.StrToIntPos(TestNums, arr[j], i);
           INC(j);
        END;
    END Fill;

BEGIN
    Fill(data);
    (* now sort *)
    o := 9;
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
    FOR i := 0 TO 9 DO
        Out.Int(data[i], 0);
        Out.String(", ");
    END;
    Out.Ln;
END BubbleSort.
