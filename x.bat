@echo off
cd D:\Software\atcoder\test\%1
7z x %1.zip
del %1.zip
call ac
call m %1
