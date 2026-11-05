@echo off
cd /d "%~dp0"
python -m trenchlab report %*
pause
