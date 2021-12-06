package main
import "fmt"

// 3. Reduce codes by using array
func main() {

    // Input data
    var input int
    fmt.Scanln(&input)

    // Determine the alphabet by using array
    alphabet := [5]string{"F", "D", "C", "B", "A"}
    var grade string
    grade = alphabet[input / 10 - 5]

    // Determine the sign
    if (grade != "F") {
        if (input % 10 >= 5) {
            grade += "+"
        } else {
            grade += "0"
        }
    }

    // Output the result
    fmt.Println(grade)
}