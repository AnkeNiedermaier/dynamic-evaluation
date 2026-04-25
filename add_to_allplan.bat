@echo off
REM This script will place symbolic link in your ALLLPLAN Usr or Std directory pointing to this repository
REM for testing purposes
set /p action="Do you want to install (i) or remove (R) the links? "
set /p targetPath="Please enter the Path to Usr or Std (with trailing \): "


if exist "%targetPath%Library\Allplan GmbH\EcoBalance.pyp" (
    del "%targetPath%Library\Allplan GmbH\EcoBalance.pyp"
)

if exist "%targetPath%Library\Allplan GmbH\EcoBalance.svg" (
    del "%targetPath%Library\Allplan GmbH\EcoBalance.svg"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\EcoBalance.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\EcoBalance.py"
)

if exist "%targetPath%Library\Allplan GmbH\EcoBalance.png" (
    del "%targetPath%Library\Allplan GmbH\EcoBalance.png"
)

if exist "%targetPath%Library\Allplan GmbH\Ecobaudat_Database.xlsx" (
    del "%targetPath%Library\Allplan GmbH\Ecobaudat_Database.xlsx"
)

if exist "%targetPath%Library\Allplan GmbH\EcoBalance_deu.xml" (
    del "%targetPath%Library\Allplan GmbH\EcoBalance_deu.xml
)

if exist "%targetPath%Library\Allplan GmbH\EcoBalance_eng.xml" (
    del "%targetPath%Library\Allplan GmbH\EcoBalance_eng.xml"
)


echo "Removal process completed"


if /I "%action%"=="i" (
    goto :install
) else if /I "%action%"=="R" (
    echo "Press any key to continue."
    pause >null
    exit /b 0
)

:install

set scriptDir=%~dp0

if not exist "%targetPath%\PythonPartsScripts" (
    mkdir "%targetPath%\PythonPartsScripts"
)

if not exist "%targetPath%\Library\Allplan GmbH" (
    mkdir "%targetPath%\Library\Allplan GmbH"
)

if not exist "%targetPath%\PythonPartsScripts\allplan_gmbh" (
    mkdir "%targetPath%\PythonPartsScripts\allplan_gmbh"
)

mklink "%targetPath%Library\Allplan GmbH\EcoBalance.svg" "%scriptDir%Library\Allplan GmbH\EcoBalance.svg"
mklink "%targetPath%Library\Allplan GmbH\EcoBalance.pyp" "%scriptDir%Library\Allplan GmbH\EcoBalance.pyp"

mklink "%targetPath%Library\Allplan GmbH\Ecobaudat_Database.xlsx" "%scriptDir%Library\Allplan GmbH\Ecobaudat_Database.xlsx"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\EcoBalance.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\EcoBalance.py"
mklink "%targetPath%Library\Allplan GmbH\EcoBalance_deu.xml" "%scriptDir%Library\Allplan GmbH\EcoBalance_deu.xml"
mklink "%targetPath%Library\Allplan GmbH\EcoBalance_eng.xml" "%scriptDir%Library\Allplan GmbH\EcoBalance_eng.xml"

echo "PythonPart installed in Allplan. You'll find it in Library -> Office or Private -> Plugin Hub."
echo "Press any key to continue"
pause >nul
exit /b 0