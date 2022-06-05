# My VBA Practice

VBA, maybe it could my ancient future

- [`ByRef` vs `ByVal` (2022.06.05)](#byref-vs-byval-20220605)
- [Declare Plural Variable (2022.06.03)](#declare-plural-variable-20220603)
- [Color Scroll 2 (2021.12.01)](#color-scroll-2-20211201)
- [Variable Scope (2011.11.29)](#variable-scope-20111129)
- [Control Formula Calculation Option (2021.11.08)](#control-formula-calculation-option-20211108)
- [Read Binary File (2021.08.23)](#read-binary-file-20210823)
- [Try ~ Catch ~ Finally (2021.07.28)](#try-catch-finally-20210728)
- [Sigma4 (2021.07.26)](#sigma4-20210726)
- [Sigma3 (2021.07.07)](#sigma3-20210707)
- [Sigma2 (2021.01.03)](#sigma2-20210103)
- [Sigma (2021.01.02)](#sigma-20210102)
- [Color Scroll (2020.11.14)](#color-scroll-20201114)


## [`ByRef` vs `ByVal` (2022.06.05)](#my-vba-practice)

- One more technical issue, following the below topic, raised from [Idea Generator v0.20 (2022.06.03)](https://github.com/kimpro82/MyFamilyCare/tree/main/IdeaGenerator#idea-generator-v020-20220603)
- Don't ignore VBA users! We also understand the difference between **Call by Reference** and **Call by Value**!
- Further discussion  
  · [[Microsoft Docs] VBA > Array argument must be ByRef](https://docs.microsoft.com/ko-kr/office/vba/language/reference/user-interface-help/array-argument-must-be-byref)  
  · [[Microsoft Docs] VBA > Understanding parameter arrays](https://docs.microsoft.com/ko-kr/office/vba/language/concepts/getting-started/understanding-parameter-arrays)

```vba
Option Explicit
```
```vba
Private Function fByRef(ByRef s As String)

    s = "바보"

End Function
```
```vba
Private Function fByVal(ByVal s As String)                  ' An array as a parameter can't be called by Value

    s = "바보"

End Function
```
```vba
Private Sub Main()

    Dim 마누라(1) As String
    Dim 남편(1) As String

    마누라(0) = "마누라"
    마누라(1) = "최고"
    남편(0) = "남편"
    남편(1) = "최고"

    Call fByRef(마누라(1))
    Call fByVal(남편(1))

    Debug.Print 마누라(0) & "는 " & 마누라(1) & "다."
    Debug.Print 남편(0) & "은 " & 남편(1) & "다."

End Sub
```
> 마누라는 바보다.  
> 남편은 최고다.


## [Declare Plural Variable (2022.06.03)](#my-vba-practice)

- A technical issue raised from [Idea Generator v0.20 (2022.06.03)](https://github.com/kimpro82/MyFamilyCare/tree/main/IdeaGenerator#idea-generator-v020-20220603)
- **Every variable should be specified individually as its type although they are declared in a line.**
- In the below cases, the result `0` means `Empty (uninitialized)` and `2` does `Integer` from `VarType()`.  
  ※ Reference ☞ [[Microsoft Docs] VBA > VarType function > Return values](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/vartype-function#return-values)

```vba
Option Explicit
```

```vba
Private Sub StupidDeclare()

    Dim a, b As Integer

    Debug.Print VarType(a) & " " & VarType(b)

End Sub
```
> 0 2

```vba
Private Sub SmartDeclare()

    Dim a As Integer, b As Integer

    Debug.Print VarType(a) & " " & VarType(b)

End Sub
```
> 2 2


## [Color Scroll 2 (2021.12.01)](#my-vba-practice)

- Advanced from [Color Scroll (2020.11.14)](#color-scroll-20201114) : succeed in making it move!
- Use `array` `Application.Calculation` `RGB()`, without `Select`/`Selection`

![Color Scroll 2](Images/VBA_ColorScroll2.gif)

```vba
Option Explicit

'Private Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal Milliseconds As LongPtr)   ' actually it is somewhat crazy to declare it as Private
```

```vba
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
```

```vba
Sub Reset()
'Initialize the sheet

    Cells.Select
    Selection.Clear

    Selection.ColumnWidth = 1
    Selection.RowHeight = 10
    Cells(1, 1).RowHeight = 409                                                     ' 409 : the max row height supported by Excel

End Sub
```


## [Variable Scope (2011.11.29)](#my-vba-practice)

- Load several operation results into `Public` variables and call them into local `Sub` procedure
- I don't think it is an enough practice but my front line now here ……

![Variable Scope](Images/VBA_Scope.gif)

```vba
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
```

```vba
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
```


## [Control Formula Calculation Option (2021.11.08)](#my-vba-practice)

- Control **Excel's formula calculation option** by `Application.Calculation` method
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


## [Read Binary File (2021.08.23)](#my-vba-practice)

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


## [Try Catch Finally (2021.07.28)](#my-vba-practice)

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


## [Sigma4 (2021.07.26)](#my-vba-practice)

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


## [Sigma3 (2021.07.07)](#my-vba-practice)

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


## [Sigma2 (2021.01.03)](#my-vba-practice)

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


## [Sigma (2021.01.02)](#my-vba-practice)

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


## [Color Scroll (2020.11.14)](#my-vba-practice)

- Make a color matrix by `Nested For` statement
- Want to make it flow, but it doesn't work well yet

![Color Scroll](Images/VBA_ColorScroll.PNG)

```vba
Option Explicit
```

```vba
Sub ColorScroll()

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

'    Differnt result from debugging mode and normal run mode(F5)
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