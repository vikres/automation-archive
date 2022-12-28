#MaxThreadsPerHotkey 2
F1::
go := !go
Send {m down}
Send {d down}
;Send {g down}
dick == 0
While go {
 Sleep, 2000
 Send {s}
 dick == dick+1
 if dick > 2:
   dick == 0
    Send {c}
}
Send {m up}
Send {d up}
;Send {g up}
Return
