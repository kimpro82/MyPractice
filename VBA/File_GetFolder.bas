' Reference ☞ https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/folder-object


Option Explicit


Sub GetFileList()

    ' Set zero point to print
    Dim printZero As Range
    Set printZero = Range("A5")

    ' Clear area to print
    Dim usingArea As Range
    Set usingArea = Range(printZero, printZero.Offset(10000, 3))
    usingArea.ClearContents

    ' Get path
    Dim oFSO, oFolder, oFile
    Dim i As Integer

    Dim path As String
    If Range("B1").Value <> "" Then
        path = Range("B1").Value
    Else
        path = ThisWorkbook.path & Application.PathSeparator
    End If
        ' Debug.Print path

    ' Get oFile collection's informations
    Set oFSO = CreateObject("Scripting.FileSystemObject")
    Set oFolder = oFSO.GetFolder(path)
        ' Debug.Print oFolder.Name
    For Each oFile In oFolder.Files                                             ' .Files property returns a Files collection consisting of all File objects
        Cells(5 + i, 1) = oFile.Name
        Cells(5 + i, 2) = oFile.Type
        Cells(5 + i, 3) = oFile.Size
        Cells(5 + i, 4) = oFile.DateCreated
        i = i + 1
    Next oFile

End Sub


Private Sub btnGetFileList_Click()

    Application.Calculation = xlManual
        Call GetFileList
    Application.Calculation = xlAutomatic

End Sub