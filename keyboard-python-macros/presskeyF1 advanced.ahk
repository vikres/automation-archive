#MaxThreadsPerHotkey 2
F1::
go := !go
Send {m down}
Send {d down}
Send {g down}
dick := 0
While go {
   Sleep, 1000
   Send {s}
   dick := %dick% + 1
   if (dick > 9) {
      Send {f}
      go := !go
      Send {d up}
      Send {g up}
      Sleep, 2000
      Send {c}
      Send {m up}
   }
}
Send {m up}
Send {d up}
Send {g up}
Return
