@echo off
g++ ..\src\main.cpp -o ..\build\a.exe && python test.py c %1
