@echo off

if "%1" == "" (
    call gcc ..\src\main.c -o ..\build\c.exe && ..\build\c.exe  < ..\src\in.txt
) else (
    python atcoder.py c %1 %2 %3 %4 %5 %6 %7 %8 %9
)
