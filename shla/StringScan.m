(* ETH Oberon, Copyright 2001 ETH Zuerich Institut fuer Computersysteme, ETH Zentrum, CH-8092 Zuerich.
Refer to the "General ETH Oberon System Source License" contract available at: http://www.oberon.ethz.ch/ *)

MODULE StringScan;

(** Convert a string into an integer. Leading white space characters are ignored. *)
	PROCEDURE StrToInt*(CONST str: ARRAY OF CHAR; VAR val: INTEGER);
		VAR i, d: INTEGER; ch: CHAR; neg: BOOLEAN;
	BEGIN
		i := 0; ch := str[0];
		WHILE (ch # 0X) & (ch <= " ") DO
			INC(i); ch := str[i]
		END;
		neg := FALSE; IF ch = "+" THEN INC(i); ch := str[i] END;
		IF ch = "-" THEN neg := TRUE; INC(i); ch := str[i] END;
		WHILE (ch # 0X) & (ch <= " ") DO
			INC(i); ch := str[i]
		END;
		val := 0;
		WHILE (ch >= "0") & (ch <= "9") DO
			d := ORD(ch)-ORD("0");
			INC(i); ch := str[i];
			IF val <= ((MAX(INTEGER)-d) DIV 10) THEN
				val := 10*val+d
			ELSIF neg & (val = 214748364) & (d = 8) & ((ch < "0") OR (ch > "9")) THEN
				val := MIN(INTEGER); neg := FALSE
			ELSE
				HALT(99)
			END
		END;
		IF neg THEN val := -val END
	END StrToInt;

(** Convert the substring beginning at position i in str into an integer. Any leading whitespace characters are ignored.
	After the conversion i pointes to the first character after the integer. *)
	PROCEDURE StrToIntPos*(CONST str: ARRAY OF CHAR; VAR val: INTEGER; VAR i: INTEGER);
		VAR noStr: ARRAY 16 OF CHAR;
	BEGIN
		WHILE (str[i] # 0X) & (str[i] <= " ") DO
			INC(i)
		END;
		val := 0;
		IF str[i] = "-" THEN
			noStr[val] := str[i]; INC(val); INC(i);
			WHILE (str[i] # 0X) & (str[i] <= " ") DO
				INC(i)
			END
		END;
		WHILE (str[i] >= "0") & (str[i] <= "9") DO
			noStr[val] := str[i]; INC(val); INC(i)
		END;
		noStr[val] := 0X;
		StrToInt(noStr, val)
	END StrToIntPos;

BEGIN
	(* -- *)
END StringScan.
