#MaxThreadsPerHotkey 2
F1::
go := !go
While go {
 Send {m down}
}
Send {m up}
Return
