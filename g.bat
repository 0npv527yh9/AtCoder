@echo off

if "%1" == "" (
  call g++ ..\src\main.cpp -o ..\build\cpp.exe -I ..\alc\ac-library && ..\build\cpp.exe < ..\src\in.txt
) else (
  python atcoder.py %contest% %1 c++ "%2"
)
