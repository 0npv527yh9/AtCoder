@echo off

setlocal enabledelayedexpansion

set type=%1
set contest=%2
set root=..\AHC\AHC!contest!

if !type! == create (
    cargo run --manifest-path !root!\Cargo.toml --release --bin gen !root!\seeds.txt
) else if !type! == test (
    set input=!root!\in\%3.txt
    set output=!root!\out\%3.txt
    set cmd=%4

    cp !input! ..\src\in.txt
    if not exist !root!\out (
        md !root!\out
    )
    call !cmd!.bat > !output! 

    cargo run --manifest-path !root!\Cargo.toml --release --bin vis !input! !output! && mv out.svg !root!\out.svg && !root!\vis.html
)

endlocal
