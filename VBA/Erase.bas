' Practice : Erase statement
' 20230103


Option Explicit


Private Sub Main()

    Dim T800(1 To 9)    As Integer
    Dim T1000()         As Integer

    Dim i As Integer, j As Integer, str As String

    ' 1. Static Array
    ' 1.1 Fill the array
    For i = 1 To 9
        T800(i) = i
    Next i

    ' 1.2 Print the array
    str = ""
    For i = 1 To 9
        str = str & T800(i)
    Next i
    Debug.Print str                                         ' 123456789

    ' 1.3 Erase the fixed array
    Erase T800

    ' 1.4 Print the array after erased
    str = ""
    For i = 1 To 9
        str = str & T800(i)
    Next i
    Debug.Print str                                         ' 000000000

    ' 2. Dynamic Array
    ' 2.1 Fill the array
    ReDim T1000(1 To 9)
    For i = 1 To 9
        T1000(i) = i
    Next i

    ' 2.2 Print the array
    str = ""
    For i = 1 To 9
        str = str & T1000(i)
    Next i
    Debug.Print str                                         ' 123456789

    ' 2.3 Erase the fixed array
    Erase T1000                                             ' become Integer()

    ' 2.4 Print the array after erased
'    str = ""
'    For i = 1 To 9
'        str = str & T1000(i)                               ' error
'    Next i
'    Debug.Print LBound(T1000) & " " & UBound(T1000)        ' error

End Sub