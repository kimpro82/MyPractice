package main
import "fmt"

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