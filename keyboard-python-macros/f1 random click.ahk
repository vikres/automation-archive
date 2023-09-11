#MaxThreadsPerHotkey,2
+::
t:=!t
While (t){
	Click down
	SLeep 20
	Click up
	Random, rand, 570, 710
	Sleep % rand
}
return