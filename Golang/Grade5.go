package main
import "fmt"

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