#include <stdio.h>

int add(a, b)                           // K&R 스타일 함수 선언: 매개변수 이름을 생략하고 데이터 타입만 표시
    int a, b;                           // 실제 매개변수 이름과 데이터 타입은 별도로 기술
{
    return a + b;
}

int add2(int a, int b)                  // ANSI C 스타일 함수 선언: 매개변수와 데이터 타입을 함께 명시
{
    return a + b;
}

int main()
{
    int result = add(5, 3);              // K&R 스타일 함수 호출
    int result2 = add2(5, 3);            // ANSI C 스타일 함수 호출

    printf("Result  (K&R) : %d\n", result);
    printf("Result2 (ANSI): %d\n", result2);
    return 0;
}
