@echo off
cd ..\test\%1
del * /S /Q > nul
7z x ..\%1.zip
del ..\%1.zip
call ac
call m %1
