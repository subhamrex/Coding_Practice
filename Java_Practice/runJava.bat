@echo off
cd %1
set name=%2
set file=%name%.class
if exist %file% (del %file%)
javac %3
if exist %file% (java %name%)
@echo.
pause
 