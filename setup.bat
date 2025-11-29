@echo off
echo ========================================
echo    MediSurge AI - Quick Start Script
echo ========================================
echo.

echo [1/4] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11 or higher
    pause
    exit /b 1
)
echo.

echo [2/4] Installing backend dependencies...
cd backend
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install backend dependencies
    pause
    exit /b 1
)
echo.

echo [3/4] Installing frontend dependencies...
cd ..\frontend
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install frontend dependencies
    pause
    exit /b 1
)
echo.

echo [4/4] Setup complete!
echo.
echo ========================================
echo       Ready to Start MediSurge AI
echo ========================================
echo.
echo To start the system:
echo   1. Backend:  cd backend  ^&  python main.py
echo   2. Frontend: cd frontend ^&  npm run dev
echo.
echo Then open: http://localhost:3000
echo.
pause
