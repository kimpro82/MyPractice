@echo off

set name=OptimizePractice
set options=O0 O1 O2 O3 Os Ofast
@REM There should be no space on the both side of "="

for %%i in (%options%) do (
    @REM echo %%i
    gcc -%%i -S %name%.c -o %name%_%%i.s
)

:: Old version
@REM gcc -O0 -S OptimizePractice.c -o OptimizePractice_O0.s
@REM gcc -O1 -S OptimizePractice.c -o OptimizePractice_O1.s
@REM gcc -O2 -S OptimizePractice.c -o OptimizePractice_O2.s
@REM gcc -O3 -S OptimizePractice.c -o OptimizePractice_O3.s
@REM gcc -Os -S OptimizePractice.c -o OptimizePractice_Os.s
@REM gcc -Ofast -S OptimizePractice.c -o OptimizePractice_Ofast.s