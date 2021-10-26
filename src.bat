@echo off
if exist ..\src\%1 (
    code ..\src\%1
) else (
    cd ..\src
)
