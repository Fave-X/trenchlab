@echo off
cd /d "%~dp0"
python -m trenchlab scan %*
pause
