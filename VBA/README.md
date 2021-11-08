# My VBA Practice

VBA, maybe it could my ancient future

- [Control Formula Calculation Option (2021.11.08)](/VBA#control-formula-calculation-option-20211108)
- [Read Binary File (2021.08.23)](/VBA#read-binary-file-20210823)
- [Try ~ Catch ~ Finally (2021.07.28)](/VBA#try-catch-finally-20210728)
- [Sigma4 (2021.07.26)](/VBA#sigma4-20210726)
- [Sigma3 (2021.07.07)](/VBA#sigma3-20210707)
- [Sigma2 (2021.01.03)](/VBA#sigma2-20210103)
- [Sigma (2021.01.02)](/VBA#sigma-20210102)
- [Color Scroll (2020.11.14)](/VBA#color_scroll-20201114)


## [Control Formula Calculation Option (2021.11.08)](/VBA#my-vba-practice)

- Control excel's formula calculation option by `Application.Calculation` method
- Working with `xlManual` status is much faster than `xlAutomatic`

```VBA
Option Explicit
```

![VBA Formula Calc. Option = xlAutomatic](Images/VBA_FormulaCalcOption_xlAutomatic.gif)

```VBA
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
```

![VBA Formula Calc. Option = xlManual](Images/VBA_FormulaCalcOption_xlManual.gif)

```VBA
' Skip excel formula calculation temporarily
Sub SkipFormulaCalc()

    Application.Calculation = xlManual
        Call sampleWork
    Application.Calculation = xlAutomatic
    
End Sub
```


## [Read Binary File (2021.08.23)](/VBA#my-vba-practice)

- Use `Open ~ For ~ As` statement
- `path` requires absoulte one

#### Trial 1

```vba
Option Explicit


Sub ReadBinaryFile()

    'Call the target file's path that user entered
    Dim path As String
    path = Range("B1")

    'Check if the file exists
    Dim fileChk As Boolean                      'default : False
    If (Len(Dir(path)) > 0) Then fileChk = True
    Range("B2") = fileChk

    Dim fn As Integer                           'fn : file number
    fn = FreeFile

    Dim output As Range
    Set output = Range("B5")                    'set offset location for output

    Open path For Binary Access Read As #fn
    
        Dim pos, posEnd As Integer
        pos = 1
        posEnd = 10
        
        Dim data As Byte

        While pos <= posEnd
            Get #fn, pos, data
            output.Offset(0, pos).Value = data
            pos = pos + 1
        Wend

    Close #fn

End Sub
```

☞ `data` doesn't work well.

![Read Binary 1](Images/VBA_ReadBinary_1.PNG)

![Read Binary - Debug](Images/VBA_ReadBinary_Debug.PNG)

#### Trial 2

☞ receive advice from [Can't read binary file data (StackOverflow)](https://stackoverflow.com/questions/68892076/cant-read-binary-file-data)

Before :
```vba
path = Range("B1")
```

After : 
```vba
path = ThisWorkbook.path & Application.PathSeparator & Range("B1")
```

![Read Binary 2](Images/VBA_ReadBinary_2.PNG)


## [Try Catch Finally (2021.07.28)](/VBA#my-vba-practice)

- Use `Try ~ Catch ~ Finally` statement in VBA
- Actually VBA doesn't support it officially, but we can imitate it with **label** based on `GoTo` grammar.

![TryCatchFinally](Images/VBA_TryCatchFinally.PNG)

![TryCatchFinally_ErrorMsgBox](Images/VBA_TryCatchFinally_ErrorMsgBox.PNG)

```vba
Option Explicit


Function Divide(a As Integer, b As Integer) As Integer

Try:                                                ' the below lines will run regardless of this
    
    On Error GoTo Catch
        Divide = a / b                              ' occurs en error when b = 0 or any possible cases (I can't imagine but ……)
    
    GoTo Finally                                    ' pass Catch: when it doesn't occur an error
    
Catch:
    
    If b = 0 Then
        MsgBox "An error occurs : division by zero."
'    Else                                           ' When b is not entered, it calls 0 as a default value.
'        MsgBox "An error occurs."
    End If
    
    Exit Function                                   ' need not to run under Finally:

Finally:
    
    MsgBox Divide                                   ' I have no any other idea to use Finally:

End Function
```


## [Sigma4 (2021.07.26)](/VBA#my-vba-practice)

- Change the calculation method from loop to **[Faulhaber's Formula](https://en.wikipedia.org/wiki/Faulhaber%27s_formula)** (make faster)
- Support operations for k ~ k^4

![Sigma4](Images/VBA_Sigma4.PNG)

![Sigma4_ErrorMsgBox1](Images/VBA_Sigma4_ErrorMsgBox1.PNG)

![Sigma4_ErrorMsgBox2](Images/VBA_Sigma4_ErrorMsgBox2.PNG)

```vba
Option Explicit

Function Sigma4(p As Integer, a As Integer, n As Integer) As Integer

    On Error GoTo ErrorHandler1

        If a > n Then
            Err.Raise 380   'Error Code 380 : Invalid property value.
        End If

    On Error GoTo ErrorHandler2

        Dim sum As Integer

        If p = 1 Then
            sum = n * (n + 1) / 2 - (a - 1) * a / 2
        ElseIf p = 2 Then
            sum = n * (n + 1) * (2 * n + 1) / 6 - (a - 1) * a * (2 * (a - 1) + 1) / 6
        ElseIf p = 3 Then
            sum = (n * (n + 1) / 2) ^ 2 - ((a - 1) * a / 2) ^ 2
        ElseIf p = 4 Then
            sum = n * (n + 1) * (2 * n + 1) * (3 * n ^ 2 + 3 * n - 1) / 30 - (a - 1) * a * (2 * (a - 1) + 1) * (3 * (a - 1) ^ 2 + 3 * (a - 1) - 1) / 30
        Else                'When p > 4
            Err.Raise 380
        End If

        Sigma4 = sum
    
    Exit Function

    ErrorHandler1:

        MsgBox "An error occurs : Starting number a is greater than final number n."

    Exit Function

    ErrorHandler2:

        MsgBox "An error occurs : Sigma4() supports only power numbers under 5."

End Function
```


## [Sigma3 (2021.07.07)](/VBA#my-vba-practice)

- Add **Error Handler** 
- How about naming labels such like `try` ~ `catch` ~ `finally`?

![Sigma3](Images/VBA_Sigma3.PNG)

![Sigma3_ErrorMsgBox](Images/VBA_Sigma3_ErrorMsgBox.PNG)

```vba
Option Explicit


Function Sigma3(k As Integer, n As Integer) As Integer

    On Error GoTo ErrorHandler

    If k > n Then
        Err.Raise 380   'Error Code 380 : Invalid property value.
    End If

    Dim i As Integer, Sum As Integer

    For i = k To n      'including both of k and n
        Sum = Sum + i
    Next i

    Sigma3 = Sum
    
    Exit Function
    

ErrorHandler:
    
    MsgBox "Error occurs : Starting number k is greater than final number n."
    
End Function
```


## [Sigma2 (2021.01.03)](/VBA#my-vba-practice)

- Add a parameter of _k_ that indicates a starting point
- Need to add codes for handling errors.

![Sigma2](Images/VBA_Sigma2.PNG)

```vba
Option Explicit


Function Sigma2(k As Integer, n As Integer) As Integer

    Dim i As Integer, Sum As Integer

    For i = k To n
        Sum = Sum + i
    Next i

    Sigma2 = Sum

End Function
```


## [Sigma (2021.01.02)](/VBA#my-vba-practice)

- Make a function to calculate `summation` (a.k.a. Sigma, Σ)
- Define all the variables as `integer`

![Sigma](Images/VBA_Sigma.PNG)

```vba
Option Explicit


Function Sigma(n As Integer) As Integer

    Dim i As Integer, Sum As Integer

    For i = 1 To n
        Sum = Sum + i
    Next i

    Sigma = Sum

End Function
```


## [Color_Scroll (2020.11.14)](/VBA#my-vba-practice)

- Make a color matrix by `Nested For` statement
- Want to make it flow, but it doesn't work well yet

![Color_Scroll](Images/VBA_Color_Scroll.png)

```vba
Option Explicit

Sub Color_Scroll()

    Dim StartRow As Integer, StartColumn As Integer, Width As Integer, Height As Integer
    Dim i As Integer, j As Integer, k As Integer
    Dim FirstColumn As Range, LastColumn As Range
    
    StartRow = 1
    StartColumn = 1
    Width = 56
    Height = 56
        
    Range(Cells(StartRow, StartColumn), Cells(Height, Width)).Select
    Selection.RowHeight = 10
    Selection.ColumnWidth = 1
    
    For i = 1 To Height
        For j = 1 To Width
            Cells(i, j).Interior.ColorIndex = (i + j) Mod 56 + 1
        Next j
    Next i
    
'Differnt result from debugging mode and normal run mode(F5)
'    For k = 1 To Width
'        Columns(Width).Select
'        Selection.Cut
'        Columns(1).Select
'        Selection.Insert Shift:=xlToRight
'    Next k
    
End Sub
```

```vba
Sub Reset()
'Initialize the sheet

    Cells.Select
    Selection.Clear
    
    Selection.ColumnWidth = 10
    Selection.RowHeight = 15

End Sub
```