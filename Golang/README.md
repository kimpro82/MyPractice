# My Golang Practice

  While not fond of the `{}` convention, can't give up on goroutines.


### List

  - [Assembly Practice 1 (2023.08.04)](#assembly-practice-1-20230804)
  - [Grade (2021.12.06)](#grade-20211206)


## [Assembly Practice 1 (2023.08.04)](#list)

  - A simple Go code and observe its assembly code through the process of compiling it
  - Future Improvements
    - Further explore assembly language
    - Dig more into topics related to memory, such as stacks and heaps
  - Codes
    <details open="">
      <summary>Assembler1.go</summary>

    ```go
    package main

    // import "fmt"

    func main() {
        // fmt.Println("I love assembly")
        println("I love assembly")
    }
    ```
    </details>
    <details open="">
      <summary>Terminal commands</summary>

    ```bash
    go tool compile -S assembler1.go
    ```
    </details>
    <details>
      <summary>Partial assembly codes and its interpretation by ChatGPT (1)</summary>

    ```go
    "".main STEXT size=86 args=0x0 locals=0x18 funcid=0x0
    ```
    해당 행은 Go 언어 코드에서 함수 `main`에 대한 정보를 나타내는 부분입니다. 이 행의 의미를 해석해보겠습니다:

    - `"".main`: 이 부분은 함수 `main`의 이름을 나타냅니다. Go 언어에서 함수 이름은 패키지 이름과 함수 이름을 합쳐서 표시될 수 있습니다.
    - `STEXT`: 이 부분은 이 함수가 텍스트(코드) 섹션에 속한다는 것을 나타냅니다. 함수의 코드가 여기에 저장됩니다.
    - `size=86`: 이 함수의 코드 크기가 86바이트라는 것을 나타냅니다. 이는 해당 함수가 컴파일된 후 생성된 어셈블리 코드의 크기입니다.
    - `args=0x0`: 이 함수에 전달되는 인자가 없음을 나타냅니다. 즉, 함수 `main`은 인자를 받지 않습니다.
    - `locals=0x18`: 이 함수 내에서 사용되는 로컬 변수의 크기가 0x18바이트임을 나타냅니다.
    - `funcid=0x0`: 함수의 고유 식별자를 나타냅니다. 이 값은 일반적으로 0이며, 특별한 경우에만 사용됩니다.

    이 행은 함수 `main`의 세부 정보를 표시하여 해당 함수의 특성과 구성을 알려줍니다.
    </details>
    <details>
      <summary>Partial assembly codes and its interpretation by ChatGPT (2)</summary>

    ```go
        0x0000 00000 (assembler1.go:5)  TEXT    "".main(SB), ABIInternal, $24-0
        0x0000 00000 (assembler1.go:5)  MOVQ    (TLS), CX
        0x0009 00009 (assembler1.go:5)  CMPQ    SP, 16(CX)
        0x000d 00013 (assembler1.go:5)  PCDATA  $0, $-2
        0x000d 00013 (assembler1.go:5)  JLS 79
        0x000f 00015 (assembler1.go:5)  PCDATA  $0, $-1
        0x000f 00015 (assembler1.go:5)  SUBQ    $24, SP
        0x0013 00019 (assembler1.go:5)  MOVQ    BP, 16(SP)
        0x0018 00024 (assembler1.go:5)  LEAQ    16(SP), BP
        0x001d 00029 (assembler1.go:5)  FUNCDATA    $0, gclocals·33cdeccccebe80329f1fdbee7f5874cb(SB)
        0x001d 00029 (assembler1.go:5)  FUNCDATA    $1, gclocals·33cdeccccebe80329f1fdbee7f5874cb(SB)
    ```
    이 부분은 Go 언어 코드에서 함수 `main`의 어셈블리 코드 표현을 나타내는 부분입니다. 각 행은 다양한 어셈블리 명령어와 해당 명령어의 주석으로 구성되어 있습니다. 아래에 각 행의 의미를 설명해드리겠습니다:

    1. `TEXT    "".main(SB), ABIInternal, $24-0`: 이 부분은 함수 `main`의 시작을 나타내며, 함수의 이름과 매개변수, 로컬 변수 등의 정보를 포함합니다. `ABIInternal`은 함수의 호출 규약을 의미하며, `$24-0`은 스택에서 사용되는 공간의 크기를 나타냅니다.
    2. `MOVQ    (TLS), CX`: TLS(Thread-Local Storage)에서 값을 읽어와 레지스터 `CX`에 저장하는 명령어입니다. TLS는 현재 스레드에 대한 데이터를 저장하는 영역입니다.
    3. `CMPQ    SP, 16(CX)`: 스택 포인터 `SP`의 값을 레지스터 `CX`에 있는 값과 비교하는 명령어입니다. 이는 스택 오버플로우를 검사하기 위한 것으로 보입니다.
    4. `PCDATA  $0, $-2`: PCDATA는 실행 정보를 나타내며, 이 행에서는 실행 상태 정보가 제공됩니다.
    5. `JLS 79`: 만약 이전의 CMPQ 조건이 만족되지 않으면 상대 주소 79로 이동합니다. 즉, 조건에 따라 분기하는 명령어입니다.
    6. `SUBQ    $24, SP`: 스택 포인터 `SP`를 24만큼 감소시키는 명령어로, 로컬 변수 공간을 할당하는 역할을 할 수 있습니다.
    7. `MOVQ    BP, 16(SP)`: 베이스 포인터 `BP`의 값을 스택 포인터 `SP`에서 16만큼 떨어진 위치에 저장하는 명령어로, 함수 프롤로그에서 실행됩니다.
    8. `LEAQ    16(SP), BP`: 베이스 포인터 `BP`에 스택 포인터 `SP`에서 16만큼 떨어진 위치의 주소를 저장하는 명령어입니다.
    9. `FUNCDATA    $0, gclocals·33cdeccccebe80329f1fdbee7f5874cb(SB)`: 함수에서 사용되는 로컬 변수에 대한 정보를 제공하는 명령어입니다.
    10. `FUNCDATA    $1, gclocals·33cdeccccebe80329f1fdbee7f5874cb(SB)`: 또 다른 종류의 함수 로컬 변수 정보를 제공하는 명령어입니다.

    이 부분은 함수 `main`의 어셈블리 코드로, 함수의 시작, 종료 및 로컬 변수 관리 등의 기본 동작을 나타내는 명령어들로 구성되어 있습니다.
    </details>
    <details>
      <summary>Partial assembly codes and its interpretation by ChatGPT (3)</summary>

    ```go
        0x001d 00029 (assembler1.go:7)  PCDATA  $1, $0
        0x001d 00029 (assembler1.go:7)  NOP
        0x0020 00032 (assembler1.go:7)  CALL    runtime.printlock(SB)
        0x0025 00037 (assembler1.go:7)  LEAQ    go.string."I love assembly\n"(SB), AX
        0x002c 00044 (assembler1.go:7)  MOVQ    AX, (SP)
        0x0030 00048 (assembler1.go:7)  MOVQ    $16, 8(SP)
        0x0039 00057 (assembler1.go:7)  CALL    runtime.printstring(SB)
        0x003e 00062 (assembler1.go:7)  NOP
        0x0040 00064 (assembler1.go:7)  CALL    runtime.printunlock(SB)
    ```
    위의 내용은 Go 언어 코드에서 함수 `main` 내에서 실행되는 어셈블리 코드 표현입니다. 이 코드의 명령어들을 하나씩 설명해드리겠습니다:

    1. `PCDATA  $1, $0`: PCDATA는 실행 정보를 나타내며, 이 행에서는 실행 상태 정보가 제공됩니다.
    2. `NOP`: 아무 동작도 수행하지 않는 명령어입니다. 주로 코드의 흐름 제어나 최적화 관련 목적으로 사용됩니다.
    3. `CALL    runtime.printlock(SB)`: `runtime.printlock` 함수를 호출하는 명령어입니다. 이 함수는 락을 획득하여 다른 스레드와의 동기화를 수행하는 역할을 합니다.
    4. `LEAQ    go.string."I love assembly\n"(SB), AX`: 문자열 상수 `"I love assembly\n"`의 주소를 레지스터 `AX`에 저장하는 명령어입니다.
    5. `MOVQ    AX, (SP)`: 레지스터 `AX`에 있는 값을 스택의 최상위에 저장하는 명령어입니다.
    6. `MOVQ    $16, 8(SP)`: 스택의 다음 위치에 16을 저장하는 명령어입니다.
    7. `CALL    runtime.printstring(SB)`: `runtime.printstring` 함수를 호출하여 문자열을 출력하는 명령어입니다.
    8. `NOP`: 아무 동작도 수행하지 않는 명령어입니다.
    9. `CALL    runtime.printunlock(SB)`: `runtime.printunlock` 함수를 호출하여 락을 해제하는 명령어입니다.

    이 부분은 `main` 함수 내에서 문자열을 출력하는 과정을 나타내는 어셈블리 코드로, 함수 호출, 레지스터 조작, 스택 연산 등의 기본적인 어셈블리 명령어들로 구성되어 있습니다.
    </details>
    <details>
      <summary>Partial assembly codes and its interpretation by ChatGPT (4)</summary>

    ```go
        0x0045 00069 (assembler1.go:8)  MOVQ    16(SP), BP
        0x004a 00074 (assembler1.go:8)  ADDQ    $24, SP
        0x004e 00078 (assembler1.go:8)  RET
        0x004f 00079 (assembler1.go:8)  NOP
        0x004f 00079 (assembler1.go:5)  PCDATA  $1, $-1
        0x004f 00079 (assembler1.go:5)  PCDATA  $0, $-2
        0x004f 00079 (assembler1.go:5)  CALL    runtime.morestack_noctxt(SB)
        0x0054 00084 (assembler1.go:5)  PCDATA  $0, $-1
        0x0054 00084 (assembler1.go:5)  JMP 0
    ```
    위의 내용은 Go 언어 코드에서 함수 `main`의 종료 과정과, 함수 `main` 외부에서의 어셈블리 코드 표현입니다. 이 코드의 명령어들을 하나씩 설명해드리겠습니다:

    1. `MOVQ    16(SP), BP`: 스택 포인터 `SP`에서 16만큼 떨어진 위치에 있는 값을 베이스 포인터 `BP`에 저장하는 명령어입니다. 이는 함수 프롤로그에서 저장한 `BP` 값을 복구하는 과정입니다.
    2. `ADDQ    $24, SP`: 스택 포인터 `SP`를 24만큼 증가시키는 명령어로, 로컬 변수 공간을 해제하는 역할을 할 수 있습니다.
    3. `RET`: 함수 `main`에서의 반환 명령어입니다. 이로써 `main` 함수의 실행이 종료됩니다.
    4. `NOP`: 아무 동작도 수행하지 않는 명령어입니다.
    5. `PCDATA  $1, $-1`: PCDATA는 실행 정보를 나타내며, 이 행에서는 실행 상태 정보가 제공됩니다.
    6. `PCDATA  $0, $-2`: PCDATA는 실행 정보를 나타내며, 이 행에서는 실행 상태 정보가 제공됩니다.
    7. `CALL    runtime.morestack_noctxt(SB)`: 스택 오버플로우 발생 시 실행되는 `runtime.morestack_noctxt` 함수를 호출하는 명령어입니다. 스택을 확장하는 역할을 합니다.
    8. `PCDATA  $0, $-1`: PCDATA는 실행 정보를 나타내며, 이 행에서는 실행 상태 정보가 제공됩니다.
    9. `JMP 0`: 상대 주소 0으로 분기하는 명령어로, 무한 루프를 형성하며 프로그램을 종료시키지 않고 계속 실행될 수 있게 합니다.

    이 부분은 함수 `main`의 종료 및 프로그램의 무한 루프 관련된 어셈블리 코드로, 함수의 반환, 스택 조작 및 무한 루프 설정 등을 나타내는 명령어들로 구성되어 있습니다.
    </details>
    <details>
      <summary>Partial assembly codes and its interpretation by ChatGPT (5)</summary>

    ```go
        rel 5+4 t=17 TLS+0
        rel 33+4 t=8 runtime.printlock+0
        rel 40+4 t=16 go.string."I love assembly\n"+0
        rel 58+4 t=8 runtime.printstring+0
        rel 65+4 t=8 runtime.printunlock+0
        rel 80+4 t=8 runtime.morestack_noctxt+0
    ```
    위의 내용은 어셈블리 언어 코드에서 메모리 참조 및 상대 주소를 나타내는 정보입니다. 각 항목은 다른 위치에 있는 메모리를 참조하는 지시 사항을 의미합니다. 여기서 설명해 드리겠습니다:

    1. `rel 5+4 t=17 TLS+0`: TLS(Thread-Local Storage) 영역의 주소를 참조합니다. 상대 주소 5에서 4바이트 크기만큼 이동한 위치에 있는 TLS의 시작 주소를 의미합니다.
    2. `rel 33+4 t=8 runtime.printlock+0`: `runtime.printlock` 함수의 주소를 상대 주소 33에서 4바이트 크기만큼 이동한 위치에서 참조합니다. 이는 해당 위치에서 `runtime.printlock` 함수를 호출하는 지시를 나타냅니다.
    3. `rel 40+4 t=16 go.string."I love assembly\n"+0`: 문자열 상수 `"I love assembly\n"`의 주소를 상대 주소 40에서 4바이트 크기만큼 이동한 위치에서 참조합니다.
    4. `rel 58+4 t=8 runtime.printstring+0`: `runtime.printstring` 함수의 주소를 상대 주소 58에서 4바이트 크기만큼 이동한 위치에서 참조합니다.
    5. `rel 65+4 t=8 runtime.printunlock+0`: `runtime.printunlock` 함수의 주소를 상대 주소 65에서 4바이트 크기만큼 이동한 위치에서 참조합니다.
    6. `rel 80+4 t=8 runtime.morestack_noctxt+0`: `runtime.morestack_noctxt` 함수의 주소를 상대 주소 80에서 4바이트 크기만큼 이동한 위치에서 참조합니다.

    상대 주소와 함수 또는 상수 이름은 컴파일러가 어셈블리 언어 코드를 기계어로 변환하는 과정에서 사용하는 정보입니다. 이 정보들은 실행 시 실제 메모리 주소로 변환되어 프로그램이 올바르게 동작할 수 있도록 도와줍니다.
    </details>
    <details>
      <summary>Partial assembly codes and its interpretation by ChatGPT (6)</summary>

    ```go
    go.cuinfo.packagename. SDWARFCUINFO dupok size=0
        0x0000 6d 61 69 6e                                      main
    ""..inittask SNOPTRDATA size=24
        0x0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
        0x0010 00 00 00 00 00 00 00 00                          ........
    go.string."I love assembly" SRODATA dupok size=15
        0x0000 49 20 6c 6f 76 65 20 61 73 73 65 6d 62 6c 79     I love assembly
    go.string."I love assembly\n" SRODATA dupok size=16
        0x0000 49 20 6c 6f 76 65 20 61 73 73 65 6d 62 6c 79 0a  I love assembly.
    gclocals·33cdeccccebe80329f1fdbee7f5874cb SRODATA dupok size=8
        0x0000 01 00 00 00 00 00 00 00                          ........
    ```
    위의 내용은 Go 언어 코드의 컴파일된 바이너리에 포함된 데이터 섹션에 관한 내용입니다. 각 섹션의 의미를 설명해드리겠습니다:

    1. `go.cuinfo.packagename. SDWARFCUINFO dupok size=0`: DWARF 디버깅 정보에서 사용되는 컴파일 단위 정보(CUINFO)를 나타냅니다. 여기서는 패키지 이름을 나타내며, `main`이라는 패키지 이름을 의미합니다.
    2. `""..inittask SNOPTRDATA size=24`: 초기화 작업을 수행하는 데 사용되는 데이터를 나타냅니다. 초기화 작업에 대한 정보와 크기가 포함되어 있습니다.
    3. `go.string."I love assembly" SRODATA dupok size=15`: 문자열 상수 `"I love assembly"`의 정보를 나타냅니다. 상수의 크기와 내용이 표시됩니다.
    4. `go.string."I love assembly\n" SRODATA dupok size=16`: 문자열 상수 `"I love assembly\n"`의 정보를 나타냅니다. 상수의 크기와 내용이 표시됩니다.
    5. `gclocals·33cdeccccebe80329f1fdbee7f5874cb SRODATA dupok size=8`: 함수 내에서 사용되는 로컬 변수에 대한 정보를 나타냅니다. 해당 로컬 변수의 크기와 내용이 표시됩니다.

    이러한 섹션들은 Go 언어 코드의 컴파일된 바이너리에 포함되어, 디버깅, 문자열 상수, 로컬 변수 등의 정보를 저장하고 활용할 수 있도록 합니다.
    </details>


## [Grade (2021.12.06)](#list)

- A simple practice code to grade a score by several ways

※ All codes include the following lines. :
```go
package main
import "fmt"
```

#### Grade1.go
```go
// 1. Vanilla if statement
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the grade
    var grade string
    if (input >= 95) {
        grade = "A+"
    } else if (input >= 90) {
        grade = "A0"
    // } more conditions {
    } else {
        grade ="F"
    }

    // Output the result
    fmt.Println(grade)
}
```

#### Grade2.go
```go
// 2. Seperate processes to get the alphabet and its sign
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the alphabet
    var grade string
    if (input >= 95) {
        grade = "A+"
    } else if (input >= 90) {
        grade = "A"
    } else if (input >= 80) {
        grade = "B"
    } else if (input >= 70) {
        grade = "C"
    } else if (input >= 60) {
        grade = "D"
    } else {
        grade ="F"
    }

    // Determine the sign
    if (grade != "A+" && grade != "F") {
        if (input % 10 >= 5) {
            grade += "+"
        } else {
            grade += "0"
        }
    }

    // Output the result
    fmt.Println(grade)
}
```

#### Grade3.go
```go
// 3. Reduce codes by using array
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the alphabet by using array
    alphabet := [11]string{"F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A+"}
    var grade string
    grade = alphabet[input / 10]

    // Determine the sign
    if (grade != "A+" && grade != "F") {
        if (input % 10 >= 5) {
            grade += "+"
        } else {
            grade += "0"
        }
    }

    // Output the result
    fmt.Println(grade)
}
```

#### Grade4.go
```go
// 4. Reduce codes by ASCII value operation
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the alphabet by ASCII value operation
    var grade string
    if (input >= 95) {
        grade = "A+"
    } else if (input >= 60) {
        grade = string(int('A') + (9 - input / 10))
    } else {
        grade = "F"
    }

    // Determine the sign
    if (grade != "A+" && grade != "F") {
        if (input % 10 >= 5) {
            grade += "+"
        } else {
            grade += "0"
        }
    }

    // Output the result
    fmt.Println(grade)
}
```

#### Grade5.go
```go
// 5. Variation for 4.3 scale based on Grade3.go
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the alphabet by using array
    alphabet := [11]string{"F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A+"}
    var grade string
    grade = alphabet[(input + 3) / 10]                                              // tricky!

    // Determine the sign
    if (grade != "A+" && grade != "F") {
        if (input % 10 >= 7) {
            grade += "-"
        } else if (input % 10 >=3) {
            grade += "+"
        } else {
            grade += "0"
        }
    }

    // Output the result
    fmt.Println(grade)
}
```
> 57

> D-

Crazy~