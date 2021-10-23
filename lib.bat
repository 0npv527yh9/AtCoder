@echo off
set file=..\lib\%1.java

if exist %file% (
    code %file%
) else if "%1" == "" (
    cd ..\lib
)
