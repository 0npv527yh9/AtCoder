@echo off

set rust=C:\software\atcoder\src\rust

if "%1" == "" (
  cargo run -q --manifest-path %rust%\Cargo.toml < ..\src\in.txt
) else (
  cp %rust%\src\main.rs ..\src\main.rs > nul
  python atcoder.py rust %1 %2 %3 %4 %5 %6 %7 %8 %9
)
