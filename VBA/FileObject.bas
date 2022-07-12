' Reference ☞ https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/file-object


Option Explicit


Sub ReadDateCreated()

    Dim fs, f, s
    Dim path As String
    path = ThisWorkbook.path & Application.PathSeparator & Range("B1").Value
        'Debug.Print path
    Set fs = CreateObject("Scripting.FileSystemObject")
    Set f = fs.GetFile(path)
    s = f.DateCreated

    Range("B2").Value = s

End Sub


Private Sub btnReadDateCreated_Click()

    Application.Calculation = xlManual
        Call ReadDateCreated
    Application.Calculation = xlAutomatic

End Sub