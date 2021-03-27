@echo off

if "%1" == "" (
  call java -cp ..\src Main < ..\src\in.txt
) else (
  python atcoder.py %1 java "%2"
)
