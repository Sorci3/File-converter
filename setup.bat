@echo off
echo Installing dependencies...
pip install Pillow python-docx fpdf2 pypdf pywin32

echo.
echo Registering context menu...
python install.py

echo.
pause
