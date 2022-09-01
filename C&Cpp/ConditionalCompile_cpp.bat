:: #ifdef fileio
g++ -Dfileio conditionalcompile.cpp
a

:: #else
g++ conditionalcompile.cpp
a