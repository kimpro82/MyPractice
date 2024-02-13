'===============================================================================
' Enum Statement Practice
' 2024.02.11
'===============================================================================


Option Explicit


Private Const SHEET_NAME As String = "ENUM"


' Define enumerations for days of the week

'------------------------------------------------------------------
' Enum DaysOfWeek1
' Description: Enumerates the days of the week starting from Sunday.
'------------------------------------------------------------------
Private Enum DaysOfWeek1
    Sunday                              ' Sunday as the first day
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
End Enum

'------------------------------------------------------------------
' Enum DaysOfWeek2
' Description: Enumerates the days of the week starting from Sunday
'             and assigns numerical values starting from 1.
'------------------------------------------------------------------
Private Enum DaysOfWeek2
    Sunday = 1                          ' Sunday assigned numerical value 1
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
End Enum

'------------------------------------------------------------------
' Enum DaysOfWeek3
' Description: Enumerates the days of the week and assigns custom
'             numerical values to each day.
'------------------------------------------------------------------
Private Enum DaysOfWeek3
    Sunday = 1                          ' Sunday assigned numerical value 1
    Monday = 1                          ' Monday assigned numerical value 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 5
    Friday = 8
    Saturday = 13
End Enum

'------------------------------------------------------------------
' Enum DaysOfWeek4
' Description: Enumerates the days of the week and assigns custom
'             numerical values to each day.
'------------------------------------------------------------------
Private Enum DaysOfWeek4
    Sunday = 1
    Monday = 3
    Tuesday = 5
    Wednesday = 7
    Thursday = 6
    Friday = 4
    Saturday = 2
End Enum


' Function to iterate through each day of the week in an enum

'------------------------------------------------------------------
' TestEnumLoop
' Description: Iterates through each day of the week in the specified
'              enum and prints the result to the Immediate Window.
' Parameters:
'   - num: Integer indicating which enumeration to test.
'------------------------------------------------------------------
Sub TestEnumLoop(num As Integer)

    Dim outputText As String
    outputText = "TestEnumLoop(" & num & ") : "

    Select Case num
    Case 1
        Dim currentDay1 As DaysOfWeek1
        For currentDay1 = DaysOfWeek1.Sunday To DaysOfWeek1.Saturday
            outputText = outputText & currentDay1 & " "
        Next currentDay1
    Case 2
        Dim currentDay2 As DaysOfWeek2
        For currentDay2 = DaysOfWeek2.Sunday To DaysOfWeek2.Saturday
            outputText = outputText & currentDay2 & " "
        Next currentDay2
    Case 3
        Dim currentDay3 As DaysOfWeek3
        For currentDay3 = DaysOfWeek3.Sunday To DaysOfWeek3.Saturday
            outputText = outputText & currentDay3 & " "
        Next currentDay3
    Case 4
        Dim currentDay4 As DaysOfWeek4
        For currentDay4 = DaysOfWeek4.Sunday To DaysOfWeek4.Saturday
            outputText = outputText & currentDay4 & " "
        Next currentDay4
    Case 5
        Dim currentDay5 As DaysOfWeek1
        For currentDay5 = DaysOfWeek1.Sunday To DaysOfWeek1.Saturday
            Select Case currentDay5
                Case DaysOfWeek1.Saturday, DaysOfWeek1.Sunday
                    outputText = outputText & currentDay5 & " "
                Case Else
                    outputText = outputText & "X" & " "
            End Select
        Next currentDay5
    Case 6
        outputText = outputText & DaysOfWeek4.Sunday & " "
        outputText = outputText & DaysOfWeek4.Monday & " "
        outputText = outputText & DaysOfWeek4.Tuesday & " "
        outputText = outputText & DaysOfWeek4.Wednesday & " "
        outputText = outputText & DaysOfWeek4.Thursday & " "
        outputText = outputText & DaysOfWeek4.Friday & " "
        outputText = outputText & DaysOfWeek4.Saturday & " "
    End Select

    Debug.Print outputText

End Sub


' Main function to run all TestEnumLoop functions

'------------------------------------------------------------------
' Main
' Description: Clears the specified sheet and runs all TestEnumLoop
'              functions to test different enumerations.
'------------------------------------------------------------------
Private Sub Main()

    Sheets(SHEET_NAME).Cells.Clear      ' Clear sheet before running tests

    Call TestEnumLoop(1)
    Call TestEnumLoop(2)
    Call TestEnumLoop(3)
    Call TestEnumLoop(4)
    Call TestEnumLoop(5)
    Call TestEnumLoop(6)

End Sub
