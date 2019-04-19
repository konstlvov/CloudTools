@echo off
:LOOP 
  if EXIST cbank.bat GOTO :BANK
  cd ..
GOTO :LOOP
:BANK
