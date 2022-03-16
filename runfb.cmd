@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
echo Running phoenixbuilder.exe...
taskkill /f /im phoenixbuilder.exe
phoenixbuilder.exe --no-hash-check
exit