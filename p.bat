@echo off

if "%1" == "" (
  call python ..\src\main.py < ..\src\in.txt
) else (
  python atcoder.py python %1 %2 %3 %4 %5 %6 %7 %8 %9
)
