@echo off

if "%1" == "" (
  rustc ..\src\rust\src\main.rs -o ..\build\rust.exe && ..\build\rust.exe < ..\src\in.txt
) else (
    python atcoder.py %1 rust "%2"
)
