#include <stdio.h>

int main()
{
    int a = 1, b = 1, c = 1, d = 1, e = 1, f = 1;

    a++;
    --b;
    // no problem

    c = ++c;
    d = d++;
    // gcc - no problem
    // clang - warning: multiple unsequenced modifications to 'c' [-Wunsequenced]

    // e = ++e--;
    // ++e--;
    // f++--++;
    // f++++++;
    // gcc - error: lvalue required as increment operand
    // clang - error: expression is not assignable

    printf("Good-bye %d %d %d %d\n", a, b, c, d);

    return 0;
}