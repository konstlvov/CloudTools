// TaskSwitchXP Pro 2.0
// WheelTab Help Script: Lock/Unlock Q shortcut key for closing applications
// Written by Alexander Avdonin
// 
// Usage:
//    1) close TaskSwitchXP configuration tool
//    2) double-click the script in Windows Explorer or run from command line:
//         >WScript //nologo WheelTab.js
//    3) confirm action
//    4) restart TaskSwitchXP to apply changes


var WshShell = WScript.CreateObject ("WScript.Shell");

var Flags = 0;
var AllUsers = WshShell.RegRead("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\AllUsers");
if (AllUsers) {
	Flags = WshShell.RegRead("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\Flags");
} else {
	Flags = WshShell.RegRead("HKCU\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\Flags");
}

var BtnCode = -1;
if (Flags & 0x40000000) {
	BtnCode = WshShell.Popup("Do you want to disable Opera-style task switching (right mouse button + wheel)?", -1, "TaskSwitchXP WheelTab Script", 4 + 32);
	Flags &= ~0x40000000;
} else {
	BtnCode = WshShell.Popup("Do you want to enable Opera-style task switching (right mouse button + wheel)?", -1, "TaskSwitchXP WheelTab Script", 4 + 32);
	Flags |= 0x40000000;
}

switch (BtnCode) {
	case 6:
		if (AllUsers) {
			WshShell.RegWrite("HKLM\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\Flags", Flags, "REG_DWORD");
		} else {
			WshShell.RegWrite("HKCU\\Software\\Alexander Avdonin\\TaskSwitchXP\\2.0\\Flags", Flags, "REG_DWORD");
		}
		WshShell.Popup("Restart TaskSwitchXP to apply changes.", 10, "TaskSwitchXP WheelTab Script", 64);		
		break;
	case 7:
		break;
	case -1:
		//WScript.Echo("Is there anybody out there?");
		break;
}
