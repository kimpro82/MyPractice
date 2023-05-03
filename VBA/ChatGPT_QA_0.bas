Option Explicit


Private Type CellLocationsType

    endpoint As String
    model As String
    apiKey As String
    question As String
    answerRange As Range                                    ' Not String but Range

End Type


Private Sub SetCellLocations(ByRef thisType As CellLocationsType)

    thisType.endpoint = Range("C2").Value
    thisType.model = Range("C3").Value
    thisType.apiKey = Range("C4").Value
    thisType.question = Range("C7").Value
    Set thisType.answerRange = Range("C8")                  ' Don't forget `set`!

End Sub


Private Sub ChatGPT()

    Dim CellLocations As CellLocationsType
    Dim request As Object
    Dim request_body As String
    Dim response As String

    ' Set required data
    Call SetCellLocations(CellLocations)

    ' Clear the Answer cell
    CellLocations.answerRange.Value = ""

    ' Request ChatGPT API
    Set request = CreateObject("WinHttp.WinHttpRequest.5.1")
    request.Open "POST", "https://api.openai.com/" & CellLocations.endpoint, False
    request.SetRequestHeader "Content-Type", "application/json"
    request.SetRequestHeader "Authorization", "Bearer " & CellLocations.apiKey
    request_body = "{" & _
        """prompt"": """ & Replace(CellLocations.question, """", "\""") & """," & _
        """model"": """ & CellLocations.model & """," & _
        """max_tokens"": 4097," & _
        """n"": 1," & _
        """stop"": [""\n""]" & _
    "}"
    Debug.Print request_body
    request.Send request_body

    ' Output
    response = Replace(request.ResponseText, Chr(34), "")
    response = Replace(response, "\n", "")
    Debug.Print response
    CellLocations.answerRange.Value = response

End Sub


Private Sub btnRun_Click()

        Application.Calculation = xlManual
            Call ChatGPT
        Application.Calculation = xlAutomatic

End Sub
