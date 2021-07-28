Option Explicit


Function Divide(a As Integer, b As Integer) As Integer

Try:                                                ' the below lines will run regardless of this

    On Error GoTo Catch

    Divide = a / b                                  ' occurs en error when b = 0
    
    GoTo Finally                                    ' pass Catch label when it doesn't occur an error
    
Catch:

    MsgBox "An error occurs : division by zero."
    
    Exit Function                                   ' need not to run under Finally label

Finally:

    MsgBox Divide

End Function