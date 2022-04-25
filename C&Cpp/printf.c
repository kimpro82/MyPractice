#include <stdio.h>

int main()
{
    char text[] = "%d %ld %lld\n";
    printf(text, __SCHAR_MAX__, __SCHAR_MAX__, __SCHAR_MAX__);
    printf(text, __INT8_MAX__, __INT8_MAX__, __INT8_MAX__);
    printf(text, __SHRT_MAX__, __SHRT_MAX__, __SHRT_MAX__);
    printf(text, __INT16_MAX__, __INT16_MAX__, __INT16_MAX__);
    printf(text, __INT_MAX__, __INT_MAX__, __INT_MAX__);
    printf(text, __LONG_MAX__, __LONG_MAX__, __LONG_MAX__);
    printf(text, __INT32_MAX__, __INT32_MAX__, __INT32_MAX__);
    printf(text, __LONG_LONG_MAX__, __LONG_LONG_MAX__, __LONG_LONG_MAX__);
    printf(text, __INT64_MAX__, __INT64_MAX__, __INT64_MAX__);

    return 0;
}