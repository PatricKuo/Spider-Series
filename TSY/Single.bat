@echo off
cd /d %~dp1 
ren "%~nx1" "%~n1"
ren "%~n1" middle.jpg
type middle.jpg >"(Íê³É)%~nx1"
ren middle.jpg "%~nx1"
taskkill /IM cmd.exe

