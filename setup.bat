@echo off
echo Installing dependencies...
pip install Pillow python-docx fpdf2 pypdf pywin32

echo.
echo Registering context menu...
python src\install.py

echo.
pause
