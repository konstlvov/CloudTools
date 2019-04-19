rem   ����� ��������������� � �����-�����������: 
rem   CmpDebug.exe D:\Bank\MyBank\Source\BLS\MyUnit.bls
rem   ��������� ����� �� ����� �����

@echo off

if exist %~f1 goto :OK
echo : File %~f1 does not exist
GOTO :END

:OK

echo : Finding bank folder...

%~d1
CD %~p1


rem ��������� � �������� ����� �����
:LOOP 
  if EXIST cbank.bat GOTO :BANK
  cd ..
GOTO :LOOP
:BANK
rem CD
ECHO : OK

CD USER

rem ���������, ��� ���� ���� DBG__

if exist DBG__.bll GOTO :DBGBLLEXIST
echo ERROR: Can not find DBG__.bll
echo Cant compile with debug information
GOTO :END
:DBGBLLEXIST

rem CD
AddDebugInfo2 %1 %temp%
echo Compiling %~n1...
path %path%;.\..\SYSTEM;.\..\USER
.\..\EXE\bscc.exe %temp%\%~nx1 -Sprotsrv -Adefault -T. -Vdebug

rem ������ ������ ����
touch.exe %~n1.bll -t 200001010000

:END