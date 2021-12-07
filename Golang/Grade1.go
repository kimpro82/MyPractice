package main
import "fmt"

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