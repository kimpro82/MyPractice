:: #ifdef fileio
gcc -Dfileio conditionalcompile.c
a

:: #else
gcc conditionalcompile.c
a