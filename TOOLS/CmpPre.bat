@echo off

echo : Finding bank folder...

%~d1
CD %~p1


rem Переходим в корневую папку банка
:LOOP 
  if EXIST cbank.bat GOTO :BANK
  cd ..
GOTO :LOOP
:BANK
rem CD
ECHO : OK

CD USER

rem CD

path %path%;.\..\SYSTEM;.\..\USER 

%Windir%\BSSPrecompiler.exe %1 %temp%\%~nx1
.\..\EXE\bscc.exe %temp%\%~nx1 -Sprotsrv -Adefault -T. -Vdebug


:END