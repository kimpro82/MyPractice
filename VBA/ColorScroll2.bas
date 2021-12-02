Option Explicit

'Private Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal Milliseconds As LongPtr)   ' actually it is somewhat crazy to declare it as Private


Sub ColorScroll2()

    Dim width, interval As Integer
    Dim base(2), rgbCol(2) As Integer                                               ' 2 means 0 to 2 (size : 3)

    width = 96
    interval = 16

    base(0) = 0
    base(1) = 127
    base(2) = 255

    Dim i, j, k As Integer

    ' shift i times
    For i = 1 To 100

        Application.Calculation = xlManual

            ' i-th drawing
            For j = 1 To width

                ' for base(0 ~ 2)
                For k = 0 To 2

                    If (base(k) \ 256) Mod 2 = 0 Then                               ' / : don't operate as int / int
                        rgbCol(k) = base(k) Mod 256
                    Else
                        rgbCol(k) = 256 - (base(k) Mod 256)
                    End If

                    ' test
                    'Cells(2 + k, j) = rgbCol(k)

                    base(k) = base(k) + interval

                Next k

                Cells(1, j).Interior.Color = RGB(rgbCol(0), rgbCol(1), rgbCol(2))   ' not .ColorIndex

            Next j

        Application.Calculation = xlAutomatic

        base(0) = base(0) + interval                                                ' is it the best?
        base(1) = base(1) + interval
        base(2) = base(2) + interval

'        Sleep (100)

    Next i

End Sub


Sub Reset()
'Initialize the sheet

    Cells.Select
    Selection.Clear

    Selection.ColumnWidth = 1
    Selection.RowHeight = 10
    Cells(1, 1).RowHeight = 409                                                     ' 409 : the max row height supported by Excel

End Sub