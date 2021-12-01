'----------------------------------------------------------------------------------------
' Module1
Option Explicit


Public num1, num2, res(7) As Integer


Sub Operate()

    num1 = ActiveSheet.Range("B1")
    num2 = ActiveSheet.Range("B2")

    res(0) = num1 + num2
    res(1) = num1 - num2
    res(2) = num1 * num2
    res(3) = num1 / num2
    res(4) = num1 \ num2                                        ' no difference from '/' because of Integer / Integer
    res(5) = num1 Mod num2
    res(6) = num1 ^ num2
    res(7) = num1 >= num2                                       ' why -1 when num1 = 5, num2 = 2?

End Sub



'----------------------------------------------------------------------------------------
' Sheet1
Sub ReadResults()

    Dim i As Integer
    For i = 0 To 7
        ActiveSheet.Range("B" & 3 + i) = res(i)
    Next i

'    Range("B3:B10").Value = res                                ' why doesn't it work?
'    Range("B3:B10").Value = WorksheetFunction.Transpose(res)   ' it works but I want to avoid WorkSheetFunction() if possible

End Sub