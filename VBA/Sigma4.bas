Option Explicit


Function Sigma4(p As Integer, a As Integer, n As Integer) As Integer

    On Error GoTo ErrorHandler

        If a < 0 Then
            Err.Raise 380   'Error Code 380 : Invalid property value.
        End If


    Dim i As Integer, sum As Integer

    On Error GoTo ErrorHandler2

        If p = 1 Then
            sum = n * (n + 1) / 2 - (a - 1) * a / 2
        ElseIf p = 2 Then
            sum = n * (n + 1) * (2 * n + 1) / 6 - (a - 1) * a * (2 * (a - 1) + 1) / 6
        ElseIf p = 3 Then
            sum = (n * (n + 1) / 2) ^ 2 - ((a - 1) * a / 2) ^ 2
        ElseIf p = 4 Then
            sum = n * (n + 1) * (2 * n + 1) * (3 * n ^ 2 + 3 * n - 1) / 30 - (a - 1) * a * (2 * (a - 1) + 1) * (3 * (a - 1) ^ 2 + 3 * (a - 1) - 1) / 30
        ElseIf p > 4 Then
            Err.Raise       'need error number
            
        Sigma3 = sum
    
    Exit Function
    

    ErrorHandler:
    
        MsgBox "Error occurs : Starting number a is greater than final number n."
        Exit Function
    
    ErrorHandler2:

        MsgBox "Sigma4() doesn't support the power number over 4."
    
End Function