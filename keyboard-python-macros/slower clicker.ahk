;On/Off with key F1, every 100 ms
F1::SetTimer, F1 Up,% (F1:=!F1)?200:"Off"
F1 Up::Click,,,%F1%