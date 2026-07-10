@echo off
REM This script will place symbolic link in your ALLLPLAN Usr or Std directory pointing to this repository
REM for testing purposes
set /p action="Do you want to install (i) or remove (R) the links? "
set /p targetPath="Please enter the Path to Usr or Std (with trailing \): "

REM Remove existing links if they exist

REM pyp,  localization and svg files in library

if exist "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.pyp" (
    del "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.pyp"
)

if exist "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.svg" (
    del "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.svg"
)

if exist "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_eng.xml" (
    del "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_eng.xml"
)

if exist "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_deu.xml" (
    del "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_deu.xml"
)

REM py files in PythonPartsScripts

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\__init__.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\__init__.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\DynamicEval.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\DynamicEval.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\AllplanEventHooks.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\AllplanEventHooks.py"
)

REM py files for app GUI

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\__init__.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\__init__.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\GUIWindow.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\GUIWindow.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\PathFunctions.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\PathFunctions.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\connect_methods.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\connect_methods.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\table_models.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\table_models.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\widget_classes.py" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\widget_classes.py"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\gui_styles.qss" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\gui_styles.qss"
)

REM icon files for app GUI

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\allplan_logo.png" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\allplan_logo.png"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\arrow_down.png" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\arrow_down.png"
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\checkbox_cross.png" (
    del "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\checkbox_cross.png"
)

REM folders in library

if exist "%targetPath%Library\Allplan GmbH\DynamicEvaluation" (
    rmdir "%targetPath%Library\Allplan GmbH\DynamicEvaluation" /s /q
)

REM folders and subfolders in PythonPartsScripts

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation" (
    rmdir "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation" /s /q
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes" (
    rmdir "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes" /s /q
)

if exist "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons" (
    rmdir "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons" /s /q
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

REM Create links if they do not exist

REM folders in library

if not exist "%targetPath%\PythonPartsScripts" (
    mkdir "%targetPath%\PythonPartsScripts"
)

if not exist "%targetPath%\Library\Allplan GmbH" (
    mkdir "%targetPath%\Library\Allplan GmbH"
)

if not exist "%targetPath%\Library\Allplan GmbH\DynamicEvaluation" (
    mkdir "%targetPath%\Library\Allplan GmbH\DynamicEvaluation"
)

REM folders in PythonPartsScripts

if not exist "%targetPath%\PythonPartsScripts\allplan_gmbh" (
    mkdir "%targetPath%\PythonPartsScripts\allplan_gmbh"
)

if not exist "%targetPath%\PythonPartsScripts\allplan_gmbh\DynamicEvaluation" (
    mkdir "%targetPath%\PythonPartsScripts\allplan_gmbh\DynamicEvaluation"
)

if not exist "%targetPath%\PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes" (
    mkdir "%targetPath%\PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes"
)

if not exist "%targetPath%\PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons" (
    mkdir "%targetPath%\PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons"
)


REM files in library

mklink "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.svg" "%scriptDir%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.svg"
mklink "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.pyp" "%scriptDir%Library\Allplan GmbH\DynamicEvaluation\DynamicEval.pyp"
mklink "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_eng.xml" "%scriptDir%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_eng.xml"
mklink "%targetPath%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_deu.xml" "%scriptDir%Library\Allplan GmbH\DynamicEvaluation\DynamicEval_deu.xml"

REM files for the PythonPart

mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\__init__.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\__init__.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\DynamicEval.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\DynamicEval.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\AllplanEventHooks.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\AllplanEventHooks.py"

REM files for the GUI

mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\__init__.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\__init__.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\GUIWindow.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\GUIWindow.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\PathFunctions.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\PathFunctions.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\connect_methods.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\connect_methods.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\table_models.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\table_models.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\widget_classes.py" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\widget_classes.py"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\gui_styles.qss" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\gui_styles.qss"

REM icon files for the GUI
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\allplan_logo.png" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\allplan_logo.png"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\arrow_down.png" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\arrow_down.png"
mklink "%targetPath%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\checkbox_cross.png" "%scriptDir%PythonPartsScripts\allplan_gmbh\DynamicEvaluation\gui_classes\icons\checkbox_cross.png"

echo "PythonPart installed in Allplan. You'll find it in Library -> Office or Private -> Plugin Hub."
echo "Press any key to continue"
pause >nul
exit /b 0