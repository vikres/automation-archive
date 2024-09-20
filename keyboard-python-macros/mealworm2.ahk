xpos1=
xpos2=
SetMouseDelay,-1
SetBatchLines, -1
Process, Priority,, High

InputBox, howmuchbait, Bait,How much bait to use bitch?, ; Input Amount of Bait to Use
InputBox, experimental, EXPERiMENTAL,ACTIVATE EXPERIMENTAL MODE? 0 OR 1,
tooltip, Put mouse in top left corner of pond and press F1
Return
f1::
If xpos1 =  
	{
	MouseGetPos, xpos1, ypos1
	tooltip, Put mouse in bottom right corner of pond and press F1
	Return
	}
If xpos2 =  
	{
	MouseGetPos, xpos2, ypos2
	Return
	}
tooltip, fishing will begin in 3 seconds. Press F2 to end early
ComObjCreate("SAPI.SpVoice").Speak("3, 2, 1")
sleep 3000
tooltip
loop	{
	sleep 50
	PixelSearch, 1Px, 1Py, %xpos1%, %ypos1%, %xpos2%, %ypos2%, 0x4D4117, 10, Fast ; Find Fish
	if (ErrorLevel = 1)
		{
		}
	else if (ErrorLevel = 0)	
		{
        Random, ANTIBAN, 30, 40
		ClickAdjustFishY:= 1Py+=ANTIBAN
        Random, ANTIBAN, 20, 30
		ClickAdjustFishX:= 1Px+=ANTIBAN
;		if experimental = 1 {
		MouseGetPos, oldx, oldy 
;		}
		MouseClick, left, %ClickAdjustFishX%, %ClickAdjustFishY% ; Click on Fish
;		if experimental = 1 {
		MouseMove, oldx, oldy
;		}
		fishcount++	; Increase Fish Count
        Random, Loose, 1, 7
        if Loose = 1 
			{
			Random, ANTIBAN, 800, 900
			sleep ANTIBAN
		} Else 
			{
            Random, ANTIBAN, 290, 410
			sleep ANTIBAN
		}
		if fishcount = %howmuchbait%	; End Fishing if Fishcount = Bait Wanted to Use
			{
			break
			}
		}
	}	
	
f2::
Msgbox, You got %fishcount% fish ; Display number of fish caught
reload	;exitapp