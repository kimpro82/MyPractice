package main
import "fmt"

// 4. Reduce codes by ASCII value operation
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the alphabet by ASCII vlaue operation
    var grade string
    if (input >= 100) {
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