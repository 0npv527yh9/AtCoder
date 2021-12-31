@echo off

if "%1" == "" (
  call javac -d ..\build ..\src\Main.java && java -cp ..\build Main < ..\src\in.txt
) else (
  python atcoder.py java %1 %2 %3 %4 %5 %6 %7 %8 %9
)
