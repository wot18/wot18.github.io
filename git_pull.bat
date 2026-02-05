@echo off
echo  git pulling......
git pull
if %errorlevel% equ 0 (
    echo git pull OK!
) else (
    echo git pull failed!
)
pause