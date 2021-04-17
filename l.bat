@echo off
if "%1" == "" (
  python login.py
) else (
  python load_testcase.py %1 %2 %3
)
