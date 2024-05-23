# [My ShellScript Practice](../README.md#my-shellscript-practice)

Shell we dance?


### \<List>

- [`hello_world("echo")` (2024.05.23)](#hello_worldecho-20240523)
- [Get the Total Size of Folders/Files Matching Specific Criteria (2024.02.29)](#get-the-total-size-of-foldersfiles-matching-specific-criteria-20240229)



## [`hello_world("echo")` (2024.05.23)](#list)

- Just for fun ☞ [related meme](https://www.reddit.com/r/ProgrammerHumor/comments/13u2mfm/_/)
  - Other language version ☞ [Python]() [TypeScript]()
- Code and Result
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
    <summary>Result</summary>

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
- Code and Result
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

