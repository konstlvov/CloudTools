// TaskSwitchXP Pro 2.0
// ShowDelay Help Script: Set ShowDelay registry value to 100 or 0 ms
// Written by Alexander Avdonin
// 
// Usage:
//    1) close TaskSwitchXP configuration tool
//    2) double-click the script in Windows Explorer or run from command line:
//         >WScript //nologo ShowDelay.js
//    3) confirm action
//    4) restart TaskSwitchXP to apply changes


var WshShell = WScript.CreateObject ("WScript.Shell");

var ShowDelay = 0;
var AllUsers = WshShell.RegRead("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\AllUsers");
if (AllUsers) {
	ShowDelay = WshShell.RegRead("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\ShowDelay");
} else {
	ShowDelay = WshShell.RegRead("HKCU\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\ShowDelay");
}

var BtnCode = -1;
if (ShowDelay) {
	BtnCode = WshShell.Popup("Set ShowDelay registry value to 0 ms?", -1, "TaskSwitchXP ShowDelay Script", 4 + 32);
	ShowDelay = 0;
} else {
	BtnCode = WshShell.Popup("Set ShowDelay registry value to 100 ms?", -1, "TaskSwitchXP ShowDelay Script", 4 + 32);
	ShowDelay = 100;
}

switch (BtnCode) {
	case 6:
		if (AllUsers) {
			WshShell.RegWrite("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\ShowDelay", ShowDelay, "REG_DWORD");
		} else {
			WshShell.RegWrite("HKCU\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\ShowDelay", ShowDelay, "REG_DWORD");
		}
		WshShell.Popup("Restart TaskSwitchXP to apply changes.", 10, "TaskSwitchXP ShowDelay Script", 64);		
		break;
	case 7:
		break;
	case -1:
		//WScript.Echo("Is there anybody out there?");
		break;
}
