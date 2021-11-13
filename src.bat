@echo off
if "%1" == "" (
    cd ..\src
) else if exist ..\src\%1 (
    code ..\src\%1
)
