@echo off

if "%1" == "" (
    call gcc ..\src\main.c -o ..\build\a.exe && ..\build\a.exe  < ..\src\in.txt
) else (
    python atcoder.py %contest% %1 c "%2"
)
