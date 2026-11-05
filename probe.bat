@echo off
cd /d "%~dp0"
python -m trenchlab probe %*
pause
