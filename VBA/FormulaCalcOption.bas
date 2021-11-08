Option Explicit


' Make a sample case that contains many calculations
Sub sampleWork()

    ' Set range
    Dim row, rowEnd, col, colEnd As Integer
    row = 1
    rowEnd = 34
    col = row
    colEnd = rowEnd

    ' Generate formula n * n times
    While row <= rowEnd
    
        While col <= colEnd

            If (row = rowEnd And col = colEnd) Then
                Sheet1.Cells(row, col) = rowEnd * 3 - 3
            ElseIf (col = colEnd) Then
                Sheet1.Cells(row, col).FormulaR1C1 = "=R[+1]C-3"    ' 삼천포 you nahm sayin
            Else
                Sheet1.Cells(row, col).FormulaR1C1 = "=RC[+1]-3"
            End If

            col = col + 1

        Wend

        col = 1
        row = row + 1

    Wend

End Sub


' Skip excel formula calculation temporarily
Sub SkipFormulaCalc()

    Application.Calculation = xlManual
        Call sampleWork
    Application.Calculation = xlAutomatic
    
End Sub