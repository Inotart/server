@echo off
cd /d %~dp0
del robot.exe > nul
echo ת����...
pyinstaller -F robot.py
move dist\*.exe dist\..
choice /t 1 /d y /n > nul
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__
del /f /s /q *.spec
echo �����
exit