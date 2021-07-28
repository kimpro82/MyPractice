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