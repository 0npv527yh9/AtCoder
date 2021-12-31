@echo off
if "%1" == "" (
  echo D:\Software\atcoder\temp | clip
) else if "%2" == "" (
  cd ..\test\%1
  del * /S /Q > nul
  7z x ..\..\temp\%1.zip
  del ..\..\temp\%1.zip
  call ac
) else (
  cd ..
  rd /S /Q test
  md test
  cd test
  7z x ..\temp\%1.zip
  call ac
)
