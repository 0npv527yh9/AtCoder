@echo off

if "%1" == "" (
  call g++ ..\src\main.cpp -o ..\build\cpp.exe -I ..\alc\ac-library && ..\build\cpp.exe < ..\src\in.txt
) else (
  python atcoder.py c++ %1 %2 %3 %4 %5 %6 %7 %8 %9
)
