@echo off
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
  py -3 scripts\serve.py
  exit /b
)
where python >nul 2>nul
if not errorlevel 1 (
  python scripts\serve.py
  exit /b
)
if exist "E:\AI-Tools\runtime\python\python.exe" (
  "E:\AI-Tools\runtime\python\python.exe" scripts\serve.py
  exit /b
)
echo Python 3 was not found. Open index.html directly or install Python 3.
pause
