// TaskSwitchXP Pro 2.0
// UnBlockQ Help Script: Lock/Unlock Q shortcut key for closing applications
// Written by Alexander Avdonin
// 
// Usage:
//    1) close TaskSwitchXP configuration tool
//    2) double-click the script in Windows Explorer or run from command line:
//         >WScript //nologo UnlockQ.js
//    3) confirm action
//    4) restart TaskSwitchXP to apply changes


var WshShell = WScript.CreateObject ("WScript.Shell");

var FlagsList = 0;
var AllUsers = WshShell.RegRead("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\AllUsers");
if (AllUsers) {
	FlagsList = WshShell.RegRead("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\FlagsList");
} else {
	FlagsList = WshShell.RegRead("HKCU\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\FlagsList");
}

var BtnCode = -1;
if (FlagsList & 0x00001000) {
	BtnCode = WshShell.Popup("Lock Q-key for closing applications?", -1, "TaskSwitchXP UnlockQ Script", 4 + 32);
	FlagsList &= ~0x00001000;
} else {
	BtnCode = WshShell.Popup("Unlock Q-key for closing applications?", -1, "TaskSwitchXP UnlockQ Script", 4 + 32);
	FlagsList |= 0x00001000;
}

switch (BtnCode) {
	case 6:
		if (AllUsers) {
			WshShell.RegWrite("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\FlagsList", FlagsList, "REG_DWORD");
		} else {
			WshShell.RegWrite("HKCU\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\FlagsList", FlagsList, "REG_DWORD");
		}
		WshShell.Popup("Restart TaskSwitchXP to apply changes.", 10, "TaskSwitchXP UnlockQ Script", 64);		
		break;
	case 7:
		break;
	case -1:
		//WScript.Echo("Is there anybody out there?");
		break;
}
