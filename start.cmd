@echo off
echo Running robot.exe...
robot.py
choice /t 2 /d y /n 1>nul
copy /Y robot_new.exe robot.exe >nul
del robot_new.exe 2>nul
%0