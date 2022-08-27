#include <stdio.h>
#include <locale.h>

int main()
{
    // Write file
    FILE* pf1 = fopen("FileIO.txt", "w");       // w : make a new empty file
    fprintf(pf1, "My wife is crazy.\n");
    fprintf(pf1, "Really crazy.\n");
    fclose(pf1);

    // Read file
    FILE* pf2 = fopen("FileIO.txt", "r");       // r : read-only
    char txt[__INT16_MAX__];
    fread(txt, 1, __INT16_MAX__, pf2);
    printf("%s", txt);
    fclose(pf2);

    return 0;
}