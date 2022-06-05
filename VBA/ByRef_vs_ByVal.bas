' Office VBA Reference

' Understanding parameter arrays
' https://docs.microsoft.com/ko-kr/office/vba/language/concepts/getting-started/understanding-parameter-arrays

' Array argument must be ByRef
' https://docs.microsoft.com/ko-kr/office/vba/language/reference/user-interface-help/array-argument-must-be-byref


Option Explicit


Private Function fByRef(ByRef s As String)

    s = "바보"

End Function


Private Function fByVal(ByVal s As String)                  ' An array as a parameter can't be called by Value

    s = "바보"

End Function


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