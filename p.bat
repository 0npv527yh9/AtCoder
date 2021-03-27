@echo off

if "%1" == "" (
  call python ..\src\main.py < ..\src\in.txt
) else (
  python atcoder.py %1 python "%2"
)
