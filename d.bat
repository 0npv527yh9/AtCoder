@echo off
if "%2" == "" (
    echo d ^<your language^> ^<answer language^>
) else if "%1" == "%2" (
    echo Test using the same language is not supported yet
) else (
    python diff.py %1 %2
)