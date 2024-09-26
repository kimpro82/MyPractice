# [My ShellScript Practice](../README.md#my-shellscript-practice)

Shell we dance?


### \<List>

- [JScript via `cscript` on Windows : 2. Read CSV (2024.09.27)](#jscript-via-cscript-on-windows--2-read-csv-20240926)
- [JScript via `cscript` on Windows : 1. `DIR` (2024.09.26)](#jscript-via-cscript-on-windows--1-dir-20240926)
- [`helloWorld("echo")` (2024.05.23)](#helloworldecho-20240523)
- [Get the Total Size of Folders/Files Matching Specific Criteria (2024.02.29)](#get-the-total-size-of-foldersfiles-matching-specific-criteria-20240229)



## [JScript via `cscript` on Windows : 2. Read CSV (2024.09.27)](#list)

- A more advanced exercise compared to [JScript via `cscript` on Windows : 1. `DIR` (2024.09.26)](#jscript-via-cscript-on-windows--1-dir-20240926)
  - The main focus was to explore whether **JSON** could be handled as a script language in Windows, but it turned out to be **impossible**
    - JScript follows the ECMAScript standard, but it hasn’t been updated in a long time, and many commonly used JavaScript keywords are not supported
    - In short, using JavaScript as-is in the Windows script environment is not easy
  - Instead, since the tool was already in hand, practiced by reading a CSV file: successful
    - Example data source: https://www.forbes.com/forbes-400/
- Code and Results
  <details>
    <summary>Code : ReadCSV.ts</summary>

  ```ts
  const COLUMN_WIDTH: number = 24; // Fixed column width for each cell in the output
  ```
  ```ts
  // Create FileSystemObject
  var fso: any = WScript.CreateObject("Scripting.FileSystemObject");

  // Get the command-line arguments
  var args: any = WScript.Arguments;

  // Check if the CSV file path is provided as an argument
  if (args.length < 1) {
      WScript.Echo("Usage: cscript JScript_RunViaCscript.js <csvFileName>");
      WScript.Quit(1);
  }
  ```
  ```ts
  // Get the CSV file name from the argument
  var csvFileName: string = args.Item(0);

  // Get the current folder where the script is running
  var scriptFullPath: string = WScript.ScriptFullName;
  var currentFolder: string = fso.GetParentFolderName(scriptFullPath);

  // Construct the full path to the CSV file
  var csvFilePath: string = fso.BuildPath(currentFolder, csvFileName);

  // Exit early if the file doesn't exist
  if (!fso.FileExists(csvFilePath)) {
      WScript.Echo("File not found: " + csvFilePath);
      WScript.Quit(1);
  }
  ```
  ```ts
  // Function to read CSV content from file
  function readCsvFile(filePath: string): string {
      var file = fso.OpenTextFile(filePath, 1); // 1 = ForReading
      var content = file.ReadAll();
      file.Close();
      return content;
  }
  ```
  ```ts
  // Function to manually trim whitespace from both ends of a string
  function manualTrim(str: string): string {
      var start: number = 0;
      var end: number = str.length - 1;

      while (start <= end && (str.charAt(start) === ' ' || str.charAt(start) === '\t')) {
          start++;
      }
      while (end >= start && (str.charAt(end) === ' ' || str.charAt(end) === '\t')) {
          end--;
      }
      return str.substring(start, end + 1);
  }
  ```
  ```ts
  // Function to pad a string to a specified width by appending spaces
  function padString(str: string, width: number): string {
      str = manualTrim(str); // Trim the string first
      var paddedString: string = str;
      while (paddedString.length < width) {
          paddedString += " "; // Append spaces until reaching the desired width
      }
      return paddedString;
  }
  ```
  ```ts
  // Function to print the separator line
  function printSeparatorLine(columns: number) {
      var separatorLine: string = "";
      for (var i = 0; i < columns * COLUMN_WIDTH; i++) {
          separatorLine += "-";
      }
      WScript.Echo(separatorLine);
  }
  ```
  ```ts
  // Function to print headers
  function printHeaders(headers: string[]) {
      var headerOutput: string = "";
      for (var h = 0; h < headers.length; h++) {
          headerOutput += padString(headers[h], COLUMN_WIDTH);
      }
      WScript.Echo(headerOutput);
  }
  ```
  ```ts
  // Function to process CSV content
  function processCsvContent(csvContent: string) {
      var lines: string[] = csvContent.split("\r\n");
      var headers: string[] = lines[0].split(",");

      printSeparatorLine(headers.length);
      printHeaders(headers);
      printSeparatorLine(headers.length);

      for (var i = 1; i < lines.length; i++) {
          var line: string = lines[i];
          var trimmedLine: string = manualTrim(line);
          if (trimmedLine !== "") {
              var row: string[] = trimmedLine.split(",");
              var record: string = "";
              for (var j = 0; j < headers.length; j++) {
                  record += padString(row[j] ? manualTrim(row[j]) : "N/A", COLUMN_WIDTH);
              }
              WScript.Echo(record);
          }
      }

      printSeparatorLine(headers.length);
  }
  ```
  ```ts
  // Main execution flow
  var csvContent: string = readCsvFile(csvFilePath);
  processCsvContent(csvContent);
  ```
  </details>
  <details open="">
    <summary>Code : ReadCSV.js (Compiled from ReadCSV.ts)</summary>

  ```bat
  tsc ReadCSV.ts --target es5 --outDir .
  ```
  ```txt
  (code omitted)
  ```
  </details>
  <details open="">
    <summary>Run & Results</summary>

  ```bat
  cscript ReadCSV.js WealthiestAmericans_2023.csv
  ```
  ```txt
  ------------------------------------------------------------------------------------------------------------------------------------------------
  Rank                    Name                    Net Worth (Billion $)   Age                     State                   Source
  ------------------------------------------------------------------------------------------------------------------------------------------------
  1                       Elon Musk               251                     52                      Texas                   Tesla & SpaceX
  2                       Jeff Bezos              161                     59                      Washington              Amazon
  3                       Larry Ellison           158                     79                      California              Oracle
  4                       Warren Buffett          121                     93                      Nebraska                Berkshire Hathaway
  5                       Larry Page              114                     50                      California              Google
  6                       Bill Gates              111                     67                      Washington              Microsoft
  7                       Sergey Brin             110                     50                      California              Google
  8                       Mark Zuckerberg         106                     39                      California              Facebook
  9                       Steve Ballmer           101                     67                      Washington              Microsoft
  10                      Michael Bloomberg       96.3                    81                      New York                Bloomberg LP
  ……
  ------------------------------------------------------------------------------------------------------------------------------------------------
  ```
  </details>


## [JScript via `cscript` on Windows : 1. `DIR` (2024.09.26)](#list)

- Practicing JScript as a Windows scripting language, as an alternative to Batchfile or PowerShell
  - Reference : [네이버 블로그 > 릿드](https://blog.naver.com/jktk1/) > [[JS] VBS 대신에 JS 사용하기](https://blog.naver.com/jktk1/223595638352)
  - Not strictly necessary, but compiled from TypeScript
  - Basic execution of the `DIR` command: Successful
- Code and Results
  <details>
    <summary>Code : DIR.ts</summary>

  ```ts
  // Define interfaces for better type checking
  interface WScriptShell {
      Exec(command: string): WScriptExec;
  }

  interface WScriptExec {
      StdOut: {
          ReadAll(): string;
      };
  }

  // Use type assertion to tell TypeScript the type of WScript
  const shell: WScriptShell = (WScript as any).CreateObject("WScript.Shell");

  // Execute 'dir' command to list files in the current directory
  const exec: WScriptExec = shell.Exec("cmd /c dir");

  // Read the output from the command
  const output: string = exec.StdOut.ReadAll();

  // Print the output
  (WScript as any).Echo(output);
  ```
  </details>
  <details open="">
    <summary>Code : DIR.js (Compiled from DIR.ts)</summary>

  ```bat
  tsc DIR.ts --target es5 --outDir .
  ```
  ```js
  // Use type assertion to tell TypeScript the type of WScript
  var shell = WScript.CreateObject("WScript.Shell");
  // Execute 'dir' command to list files in the current directory
  var exec = shell.Exec("cmd /c dir");
  // Read the output from the command
  var output = exec.StdOut.ReadAll();
  // Print the output
  WScript.Echo(output);
  ```
  </details>
  <details open="">
    <summary>Run & Results</summary>

  ```bat
  cscript DIR.js
  ```
  ```txt
  ……

   C 드라이브의 볼륨: SSD (C:)
   볼륨 일련 번호: ****-****

   C:\**** 디렉터리

  2024-09-26  오후 04:46    <DIR>          .
  2024-09-26  오후 04:46    <DIR>          ..
  2024-09-26  오후 04:49               410 DIR.js
  2024-09-26  오후 04:49               679 DIR.ts
  2024-09-26  오후 04:45                36 DIR_Conv.bat
  2024-09-26  오후 04:46                16 DIR_Run.bat
  ……
                14개 파일              15,937 바이트
  ……
  ```
  </details>


## [`helloWorld("echo")` (2024.05.23)](#list)

- Just for fun ☞ [related meme](https://www.reddit.com/r/ProgrammerHumor/comments/13u2mfm/_/)
  - Other language version ☞ [Python](/Python/README.md#hello_worldprint-20240523) [TypeScript](https://github.com/kimpro82/MyWebPractice/blob/main/TypeScript/README.md#helloworldconsolelog-20240523)
- Code and Results
  <details>
    <summary>Code : helloWorldEcho.sh</summary>

  ```bash
  #!/bin/bash
  ```
  ```bash
  helloWorld() {
      # Retrieves the current function name and calls the given function dynamically.
      #
      # Arguments:
      #     funcName (str): The name of the function to call.
      # Returns:
      #     None
      local funcName=$1
      local currentFuncName="${FUNCNAME[0]}"

      # Invokes the function with the given name and passes the current function name as an argument.
      "$funcName" "$currentFuncName"
  }
  ```
  ```bash
  # Call the helloWorld function.
  helloWorld "echo"
  ```
  </details>
  <details open="">
    <summary>Results</summary>

  ```shell
  helloWorld
  ```
  </details>


## [Get the Total Size of Folders/Files Matching Specific Criteria (2024.02.29)](#list)

- I've been suddenly curious about these
- References
  - [Microsoft Learn](https://learn.microsoft.com/) > [Windows Server](https://learn.microsoft.com/windows-server/) > [dir](https://learn.microsoft.com/windows-server/administration/windows-commands/dir)
  - [Microsoft Learn](https://learn.microsoft.com/) > [PowerShell](https://learn.microsoft.com/powershell/) > [Get-ChildItem](https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-childitem)
  - [Wikipedia](https://en.wikipedia.org/) > [ls](https://en.wikipedia.org/wiki/Ls)
  - [Wikipedia](https://en.wikipedia.org/) > [du (Unix)](https://en.wikipedia.org/wiki/Du_(Unix))
- Code and Results
  <details>
    <summary>cmd : TotalSize.cmd</summary>

  ```cmd
  dir
  ```
  ```cmd
  C 드라이브의 볼륨: SSD (C:)
  볼륨 일련 번호: ****-****

  C:\****\MyPractice\Shell 디렉터리

  2024-03-01  오전 01:52    <DIR>          .
  2024-03-01  오전 01:52    <DIR>          ..
  2024-03-01  오전 02:13               104 TotalSize.cmd
  2024-03-01  오전 02:17               183 TotalSize.ps1
  2024-03-01  오전 02:18               164 TotalSize.sh
                3개 파일                 451 바이트
                2개 디렉터리   4,160,643,072 바이트 남음
  ```

  ```cmd
  dir *.cmd
  ```
  ```cmd
  C 드라이브의 볼륨: SSD (C:)
  볼륨 일련 번호: ****-****

  C:\****\MyPractice\Shell 디렉터리

  2024-03-01  오전 02:13               104 TotalSize.cmd
                1개 파일                 104 바이트
                0개 디렉터리   4,164,726,784 바이트 남음
  ```
  </details>
  <details>
    <summary>PowerShell : TotalSize.ps1</summary>

  ```powershell
  get-childitem
  ```
  ```powershell
      디렉터리: C:\****\MyPractice\Shell


  Mode                LastWriteTime     Length Name
  ----                -------------     ------ ----
  -a---      2024-03-01   오전 2:13        104 TotalSize.cmd
  -a---      2024-03-01   오전 2:17        183 TotalSize.ps1
  -a---      2024-03-01   오전 2:18        164 TotalSize.sh
  ```

  ```powershell
  get-childitem *.ps1
  ```
  ```powershell
  -a---      2024-03-01   오전 2:17        183 TotalSize.ps1
  ```

  ```powershell
  get-childitem | measure-object -property length -sum
  ```
  ```powershell
  Count    : 3
  Average  :
  Sum      : 451
  Maximum  :
  Minimum  :
  Property : Length
  ```
  </details>
  <details>
    <summary>Bash : TotalSize.sh</summary>

  ```bash
  ls -l
  ```
  ```bash
  total 3
  -rw-r--r-- 1 fya 197609 104 Mar  1 02:13 TotalSize.cmd
  -rw-r--r-- 1 fya 197609 183 Mar  1 02:17 TotalSize.ps1
  -rwxr-xr-x 1 fya 197609 164 Mar  1 02:18 TotalSize.sh
  ```
  
  ```bash
  du -c 
  ```
  ```bash
  3       .
  3       total
  ```
  
  ```bash
  du -ch
  ```
  ```bash
  3.0K    .
  3.0K    total
  ```

  ```bash
  du -cb
  ```
  ```bash
  451     .
  451     total
  ```

  ```bash
  du -cb *
  ```
  ```bash
  104     TotalSize.cmd
  183     TotalSize.ps1
  164     TotalSize.sh
  451     total
  ```

  ```bash
  du -cb *.sh
  ```
  ```bash
  164     TotalSize.sh
  164     total
  ```
  </details>

