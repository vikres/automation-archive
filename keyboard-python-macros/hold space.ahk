#MaxThreadsPerHotkey 2
F1::
go := !go
While go {
 Send {space down}
}
Send {space up}
Return
