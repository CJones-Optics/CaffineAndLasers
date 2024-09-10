@echo off

REM Simple script which searches for all .html files in blogsHTML
REM and converts them to .md files in blogsMD

REM Check if blogsMD exists, if not create it
IF NOT EXIST "blogsMD" (
    mkdir blogsMD
)

REM Loop through all .html files in blogsHTML
FOR %%f IN (blogsHTML\*.html) DO (
    REM Get the filename without the extension
    SET "filename=%%~nf"
    ECHO Converting %%~nxf to blogsMD\%%~nxf
    REM Convert the file to .md
    pandoc -s "%%f" -o "blogsMD\%%~nf.md"
)

