@echo off
gcc ..\src\main.c -o ..\build\a.exe && python test.py c %1
