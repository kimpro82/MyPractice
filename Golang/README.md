# My Golang Practice


- [Grade (2021.12.06)](/Golang#grade-20211206)


## [Grade (2021.12.06)](#my-golang-practice)

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
    alphabet := [6]string{"F", "D", "C", "B", "A", "A+"}
    var grade string
    grade = alphabet[input / 10 - 5]

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
> 

#### Grade4.go
```go
// 4. Reduce codes by ASCII value operation
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the alphabet by ASCII vlaue operation
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