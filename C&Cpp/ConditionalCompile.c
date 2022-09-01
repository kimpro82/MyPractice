#include <stdio.h>

int main()
{
    char txt[] = "I am your father.\n";

    #ifdef fileio
        char fileName[] = "ConditionalCompile.txt";

        FILE* pf = fopen(fileName, "w");       // w : make a new empty file
        fprintf(pf, txt);
        fclose(pf);

        printf("%s has been generated.\n", fileName);
    #else
        printf("%s", txt);
    #endif

    return 0;
}