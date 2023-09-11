#Requires AutoHotkey v2.0+

~LButton::SetTimer AutoClick, -1       ; start the auto-clicker

AutoClick()
{
    If GetKeyState("LButton", "P")     ; check to see that LButton is still pressed
    {
        Click                          ; send the click
        delay := (Random(1, 10) = 1)   ; 10% chance
               ? Random(100, 400)    ; 1 - 4 second delay
               : Random(000, 300)    ; 2 - 3 second delay
        SetTimer AutoClick,  -delay    ; set the timer to call this function again with the calculated delay
    }
}