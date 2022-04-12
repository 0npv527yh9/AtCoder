@echo off

if "%1" == "" (
  python ..\src\main.py < ..\src\in.txt
) else (
  python atcoder.py pypy %1 %2 %3 %4 %5 %6 %7 %8 %9
)
