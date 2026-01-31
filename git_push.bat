@echo off
setlocal enabledelayedexpansion

echo === Starting Git Auto Commit Script ===

:InputCommitMessage
set /p commit_msg="Please enter commit message: "

if "%commit_msg%"=="" (
    echo Error: Commit message cannot be empty!
    echo Please try again.
    goto InputCommitMessage
)

echo.
echo Executing: git add .
git add .

echo.
echo Executing: git commit -m "%commit_msg%"
git commit -m "%commit_msg%"

if %errorlevel% neq 0 (
    echo.
    echo Error: git commit failed!
    echo Possible reasons: no changes to commit or other errors.
    pause
    exit /b 1
)

echo.
echo Executing: git push
git push

echo.
echo === Script execution completed ===
pause