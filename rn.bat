@echo off
if "%1" == "" (
  echo designate %%1
) else (
  python rename.py %1
)
