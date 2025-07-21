@echo off
echo Cleaning auxiliary files...
del /q main.pdf 2>nul
del /q main.aux main.toc main.lof main.lot main.out main.log 2>nul
del /q *.aux *.toc *.lof *.lot *.out *.log 2>nul
del /q data\*.aux data\*.toc data\*.lof data\*.lot data\*.out data\*.log 2>nul

echo.
echo First compilation with xelatex...
echo Press Enter when prompted...
xelatex main.tex

echo.
echo Running bibtex...
bibtex main

echo.
echo Second compilation with xelatex...
echo Press Enter when prompted...
xelatex main.tex

echo.
echo Final compilation with xelatex...
echo Press Enter when prompted...
xelatex main.tex

echo.
echo Compilation completed!
echo Opening main.pdf...
start main.pdf
echo.
pause 