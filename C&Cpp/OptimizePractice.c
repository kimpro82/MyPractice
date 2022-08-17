#include <stdio.h>

void operate(int i, int* p)
{
    if (i % 2 != 0) (*p)++;
}

int main()
{
    int num = 0;
    int* p = &num;

    for (int i = 0; i < 10; i++) operate(i, p);

    printf("%d\n", num);

    return 0;
}