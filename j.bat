@echo off

if "%1" == "" (
  call javac -d ..\build ..\src\Main.java && java -cp ..\build Main < ..\src\in.txt
) else (
  python atcoder.py %1 java "%2"
)
