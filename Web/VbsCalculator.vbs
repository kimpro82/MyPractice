Function appendToDisplay(value)

  document.getElementById("display").value = document.getElementById("display").value & value

End Function


Function clearDisplay()

  document.getElementById("display").value = ""

End Function


Function calculateResult()

  On Error Resume Next

    result = Eval(document.getElementById("display").value)

    If Err.Number = 0 Then
        document.getElementById("display").value = result
    Else
        document.getElementById("display").value = "Error"
    End If

  On Error GoTo 0

End Function
