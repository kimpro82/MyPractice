' [Microsoft Docs] VBA > VarType function > Return values
' ☞ https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/vartype-function#return-values


Option Explicit


Private Sub StupidDeclare()

    Dim a, b As Integer

    Debug.Print VarType(a) & " " & VarType(b)

End Sub


Private Sub SmartDeclare()

    Dim a As Integer, b As Integer

    Debug.Print VarType(a) & " " & VarType(b)

End Sub