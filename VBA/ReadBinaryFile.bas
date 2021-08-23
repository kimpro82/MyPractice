Option Explicit


Sub ReadBinaryFile()

    'Call the target file's path that user entered
    Dim path As String
    path = ThisWorkbook.path & Application.PathSeparator & Range("B1")

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