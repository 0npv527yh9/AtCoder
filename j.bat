@echo off
javac -d ..\build ..\src\Main.java && python test.py java %1
