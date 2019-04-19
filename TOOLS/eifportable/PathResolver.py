# -*- coding: utf-8 -*-

import os.path
import glob

class PathResolverException(Exception):
	def __init__(self, value):
		self.value = value

class ErrRootDirNotFound(PathResolverException):
	"""docstring for ExceptionRootDirNotFound"""
	def __str__(self):
		return repr("Can'not find stand root for path: " + self.value)

class PathResolver(object):
	"""PathResolver interface"""

	@staticmethod
	def IsRoot(path):
		return os.path.exists(os.path.join(path, "exe")) and os.path.exists(os.path.join(path, "system"));

	@staticmethod
	def FindRoot(somePathInStand):
		standDir = somePathInStand if os.path.isdir(somePathInStand) else os.path.dirname(somePathInStand)
		if not PathResolver.IsRoot(standDir):
			for step in range(8):
				standDir = os.path.join(standDir, os.path.pardir)
				if PathResolver.IsRoot(standDir):
					break
			else:
				raise ErrRootDirNotFound(somePathInStand)
		return os.path.abspath(standDir)
				
	@staticmethod
	def IsEifDir(path):
		return os.path.exists(os.path.join(path, "forms")) and os.path.exists(os.path.join(path, "tables")) \
					 or len(glob.glob(os.path.join(path, "*.eif"))) > 0;

	def __init__(self, arg):
		self.__path = arg
		super(PathResolver, self).__init__()
	
	def GetRootDir(self):
		return self.FindRoot(self.__path);

	def GetBankEifDir(self):
		for resDir in [os.path.join(self.GetRootDir(), "Bank"),
		               os.path.join(self.GetRootDir(), "Base"),
							     os.path.join(self.GetRootDir(), "Base", "Bank")]:
			if self.IsEifDir(resDir):
				break
		else:
			resDir = os.path.join(self.GetRootDir(), "Bank")
		return resDir;

	def GetClientEifDir(self):
		for resDir in [os.path.join(self.GetRootDir(), "Client"),
		               os.path.join(self.GetRootDir(), "Base"),
							     os.path.join(self.GetRootDir(), "Base", "Client")]:
			if self.IsEifDir(resDir):
				break
		else:
			resDir = os.path.join(self.GetRootDir(), "Client")
		return resDir;

	def GetInetPubDir(self):
		for resDir in [os.path.join(self.GetRootDir(), "InetPub"),
		               os.path.join(self.GetRootDir(), "www")]:
			if os.path.exists(resDir):
				break
		else:
			resDir = os.path.join(self.GetRootDir(), "InetPub")
		return resDir;

	def GetSiteDir(self):
		for resDir in [os.path.join(self.GetInetPubDir(), "bsi_sites", "rt_ic"),
		               os.path.join(self.GetInetPubDir(), "bsi_sites")]:
			virtDirs = glob.glob(os.path.join(resDir, "v*", ""))
			if len(virtDirs) > 0:
				virtDirs.sort()
				resDir = os.path.abspath(virtDirs[-1])
				break
		else:
			resDir = os.path.join(self.GetInetPubDir(), "bsi_sites", "rt_ic", "v1")
		return resDir

	def GetBsiDllDir(self):
		for resDir in [os.path.join(self.GetInetPubDir(), "bsi_scripts", "rt_ic"),
		               os.path.join(self.GetInetPubDir(), "bsi_scripts")]:
			if os.path.exists(os.path.join(resDir, "bsi.dll")):
				break
		else:
			resDir = os.path.join(self.GetInetPubDir(), "bsi_scripts", "rt_ic")
		return resDir

	def GetBlsDir(self):
		for resDir in [os.path.join(self.GetRootDir(), "Source", "Bls"),
					   os.path.join(self.GetRootDir(), "Source"),
		               os.path.join(self.GetRootDir(), "Bls")]:
			if os.path.exists(resDir):
				break
		else:
			resDir = os.path.join(self.GetRootDir(), "Source", "Bls")
		return resDir

	def GetDbDir(self):
		return os.path.join(self.GetRootDir(), "Data")

	def GetExeDir(self):
		return os.path.join(self.GetRootDir(), "Exe")

	def GetSystemDir(self):
		return os.path.join(self.GetRootDir(), "System")

	def GetSubsysDir(self):
		return os.path.join(self.GetRootDir(), "Subsys")

	def GetTemplateDir(self):
		return os.path.join(self.GetSubsysDir(), "Template")

	def GetSiteTemplateDir(self):
		for resDir in [os.path.join(self.GetTemplateDir(), "rt_ic"),
		               os.path.join(self.GetTemplateDir(), "ic")]:
			if os.path.exists(resDir): break;
		else:
			resDir = os.path.join(self.GetTemplateDir(), "rt_ic")
		return resDir;

	def GetUserDir(self):
		return os.path.join(self.GetRootDir(), "User")

	def GetUpgradeDir(self):
		return os.path.join(self.GetRootDir(), "Upgrade")

	def GetUtilsDir(self):
		return os.path.join(self.GetRootDir(), "Utils")

	def GetMavenDir(self):
		return os.path.join(self.GetRootDir(), "Maven")

	def GetStandSettingsCfg(self):
		return os.path.join(self.GetRootDir(), "StandSettings.cfg")

	def GetCBank(self):
		return os.path.join(self.GetExeDir(), "cbank.exe")

	def GetDictman(self):
		return os.path.join(self.GetExeDir(), "dictman.exe")

	def GetRts(self):
		return os.path.join(self.GetExeDir(), "rts.exe")

	def GetProtcore(self):
		return os.path.join(self.GetExeDir(), "protcore.exe")

	def GetExecBll(self):
		return os.path.join(self.GetExeDir(), "execbll.exe")

	def GetBunitRunner(self):
		return os.path.join(self.GetExeDir(), "bunitrunner.exe")

	def GetBscc(self):
		return os.path.join(self.GetExeDir(), "bscc.exe")

import unittest

def testSuite():
	suite = unittest.makeSuite(MainTestCase,'test')
	return suite

class MainTestCase(unittest.TestCase):
	def testFindRoot(self):
		self.assertEqual(PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300"), "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300")
		self.assertEqual(PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK.zip"), "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300")
		self.assertEqual(PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK.zip12423423"), "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300")
		self.assertEqual(PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK"), "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300")
		self.assertEqual(PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK\\Config\\Archive(14).eif"), "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300")
		self.assertEqual(PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\InetPub\\Bsi_sites\\rt_ic\\v1\\scheme\\account\\account_scDocTbl.xsl"), "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300")
		#with self.assertRaises(ErrRootDirNotFound):
		#	assertRaisesstandRoot = PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart") 
		#with self.assertRaises(ErrRootDirNotFound):
		#	standRoot = PathResolver.FindRoot("\\\\SOZYKIN-V\\Banks\\Standart\\sm_last.log") 

	def testGetRootDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetRootDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300", "Main root isn't found"
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK.zip").GetRootDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300" , "Main file root isn't found"
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK.zip12423423").GetRootDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300" , "Main file root isn't found"
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK").GetRootDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300" , "Inner root isn't found"
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\BANK\\Config\\Archive(14).eif").GetRootDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300" , "Inner file root isn't found"
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\InetPub\\Bsi_sites\\rt_ic\\v1\\scheme\\account\\account_scDocTbl.xsl").GetRootDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300" , "Inner file root isn't found"
		#with self.assertRaises(ErrRootDirNotFound):
		#	standRoot = PathResolver("\\\\SOZYKIN-V\\Banks\\Standart").GetRootDir()
		#with self.assertRaises(ErrRootDirNotFound):
		#	standRoot = PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\sm_last.log").GetRootDir()

	def testGetBankEifDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetBankEifDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Bank", "Bank eif dir not found"

	def testGetClientEifDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetClientEifDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Client", "Client eif dir not found"

	def testGetInetPubDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetInetPubDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\InetPub", "InetPub dir not found"

	def testGetSiteDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetSiteDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\InetPub\\bsi_sites\\rt_ic\\v1", "Site dir not found"

	def testGetBlsDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetBlsDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Source\\Bls", "Source dir not found"

	def testGetDbDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetDbDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Data", "Data db dir not found"

	def testGetExeDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetExeDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe", "Exe dir not found"

	def testGetSystemDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetSystemDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\System", "System dir not found"

	def testGetSubsysDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetSubsysDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Subsys", "Subsys dir not found"

	def testGetTemplateDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetTemplateDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Subsys\\Template", "Template dir not found"

	def testGetUserDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetUserDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\User", "User dir not found"

	def testGetUpgradeDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetUpgradeDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Upgrade", "Upgrade dir not found"

	def testGetUtilsDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetUtilsDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Utils", "Utils dir not found"

	def testGetMavenDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetMavenDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Maven", "Maven dir not found"

	def testGetBsiDllDir(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetBsiDllDir() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\InetPub\\bsi_scripts\\rt_ic", "Bsi dll dir not found"

	def testGetStandSettingsCfg(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetStandSettingsCfg() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\StandSettings.cfg", "StandSettings.cfg file not found"

	def testGetCBank(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetCBank() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe\\cbank.exe", "cbank.exe file not found"

	def testGetDictman(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetDictman() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe\\dictman.exe", "dictman.exe file not found"

	def testGetRts(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetRts() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe\\rts.exe", "rts.exe file not found"

	def testGetProtcore(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetProtcore() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe\\protcore.exe", "protcore.exe file not found"

	def testGetExecBll(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetExecBll() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe\\execbll.exe", "execbll.exe file not found"

	def testGetBunitRunner(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetBunitRunner() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe\\bunitrunner.exe", "bunitrunner.exe file not found"

	def testGetBscc(self):
		assert PathResolver("\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300").GetBscc() == "\\\\SOZYKIN-V\\Banks\\Standart\\017_7_300\\Exe\\bscc.exe", "bscc.exe file not found"

if __name__ == "__main__":
	unittest.main()